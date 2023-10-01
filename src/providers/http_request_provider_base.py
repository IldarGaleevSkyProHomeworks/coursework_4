import requests

from src.abstractions import HttpRequestProvider


class HttpRequestProviderBase(HttpRequestProvider):
    """
    Basic http request provider
    """
    @classmethod
    def get_data_dict(cls, url: str, **kwargs):
        response = requests.get(url=url, **kwargs)
        return response.json()
