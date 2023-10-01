import json
import os

from src.abstractions import HttpRequestProvider


class MockVacancyProviderHeadHunter(HttpRequestProvider):
    test_data_dir = None

    @classmethod
    def get_data_dict(cls, url, **kwargs):
        print(url, kwargs)
        with open(os.path.join(cls.test_data_dir, 'head_hunter_vacancy_response.json'), encoding='UTF-8') as file:
            return json.load(file)
