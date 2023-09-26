import requests

from src.abstractions import HttpRequestProvider


class BaseHttpRequestProvider(HttpRequestProvider):
    @classmethod
    def get_data_dict(cls, url: str, **kwargs):
        response = requests.get(url=url, **kwargs)
        return response.json()
