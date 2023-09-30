import src.constants as const
from src.abstractions import VacancyProvider
from src.entities import Vacancy, Salary, Currency
from src.providers.http_request_provider_base import HttpRequestProviderBase


class VacancyProviderHeadHunter(VacancyProvider):
    http_request_provider = HttpRequestProviderBase

    _base_url = 'https://api.hh.ru'
    _generic_headers = {
        "User-Agent": f"{const.APP_NAME}/{const.APP_VER} ({const.APP_EMAIL})"
    }

    def get_raw_data(self, **kwargs):
        try:
            return self.http_request_provider.get_data_dict(
                f'{self._base_url}/vacancies',
                headers=self._generic_headers,
                **kwargs
            )
        except Exception as ex:
            raise Exception("Head Hunter API request error") from ex

    def get_vacancies(self, **kwargs) -> list[Vacancy]:

        params = {}

        if (search_text := kwargs.get('search_text', None)) is not None:
            params['text'] = search_text
            params['search_field'] = ['name', 'description']

        if (per_page := kwargs.get('per_page', None)) is not None:
            params['per_page'] = per_page

        if (page_num := kwargs.get('page_num', None)) is not None:
            params['page'] = page_num

        data = self.get_raw_data(params=params)

        result = []
        for response_item in data['items']:
            salary = response_item.get('salary', None)
            if salary is not None:
                currency_code = salary['currency']

                # TODO: probably need to implement a currency-code normalizer
                if currency_code == 'RUR':
                    currency_code = 'RUB'

                salary = Salary(
                    salary_from=None if salary['from'] is None else Currency(salary['from'], currency_code),
                    salary_to=None if salary['to'] is None else Currency(salary['to'], currency_code),
                )

            vacancy = Vacancy(
                title=response_item.get('name', None),
                # TODO probably need to remove the XML tags.
                description=response_item.get('snippet', {'responsibility': None}).get('responsibility', None),
                url=response_item.get('url', None),
                salary=salary
            )

            result.append(vacancy)

        return result

    @property
    def provider_name(self):
        return "Head Hunter"
