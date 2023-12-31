import logging
import os

import src.constants as const
from src.abstractions import VacancyProvider, SearchResult
from src.entities import Vacancy, Salary, Currency
from src.providers.http_request_provider_base import HttpRequestProviderBase


class VacancyProviderSuperjob(VacancyProvider):
    """
    Provide vacancies from SuperJob.ru
    """

    DEFAULT_PER_PAGE = 20
    API_KEY = os.getenv('API_KEY_SUPERJOB')

    module_logger = logging.getLogger('VacancyProviderSuperjob')
    http_request_provider = HttpRequestProviderBase

    _base_url = 'https://api.superjob.ru/2.0'
    _generic_headers = {
        "User-Agent": f"{const.APP_NAME}/{const.APP_VER} ({const.APP_EMAIL})",
        "X-Api-App-Id": API_KEY
    }

    def get_raw_data(self, **kwargs):
        try:
            return self.http_request_provider.get_data_dict(
                f'{self._base_url}/vacancies/',
                headers=self._generic_headers,
                **kwargs
            )
        except Exception as ex:
            raise Exception("Head Hunter API request error") from ex

    def get_vacancies(self, **kwargs) -> SearchResult:
        if self.API_KEY is None:
            self.module_logger.warning('Superjob API-Key not changed!')
            return SearchResult([], 0, 0, 0)

        params = {}

        if (search_text := kwargs.get('search_text', None)) is not None:
            params['keyword'] = search_text

        if (per_page := kwargs.get('per_page', None)) is not None:
            params['count'] = per_page

        if (page_num := kwargs.get('page_num', None)) is not None:
            params['page'] = page_num

        data = self.get_raw_data(params=params)

        result = []
        for response_item in data['objects']:
            currency_code = response_item['currency']

            salary = Salary(
                salary_from=None if response_item['payment_from'] == 0 else Currency(response_item['payment_from'],
                                                                                     currency_code),
                salary_to=None if response_item['payment_to'] == 0 else Currency(response_item['payment_to'],
                                                                                 currency_code),
            )

            vacancy = Vacancy(
                title=response_item.get('profession', None),
                # TODO probably need to remove the XML tags.
                description=response_item.get('candidat', None),
                url=response_item.get('link', None),
                salary=salary
            )

            result.append(vacancy)

        total = int(data.get('total', 0))

        if per_page is None:
            per_page = self.DEFAULT_PER_PAGE

        if page_num is None:
            page_num = 0

        page_count = round(total / per_page)

        return SearchResult(
            result_list=result,
            total_results=total,
            total_pages=page_count,
            page_num=page_num
        )

    @property
    def provider_name(self):
        return "Superjob"
