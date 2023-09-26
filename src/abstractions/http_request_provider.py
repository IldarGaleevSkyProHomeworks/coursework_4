from abc import abstractmethod, ABC


class HttpRequestProvider(ABC):
    @classmethod
    @abstractmethod
    def get_data_dict(cls, url: str, **kwargs) -> dict:
        pass


class HttpRequested:
    http_request_provider: HttpRequestProvider = None
