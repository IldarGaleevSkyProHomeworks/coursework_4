from abc import abstractmethod, ABC


class CurrencyProvider(ABC):

    @classmethod
    @abstractmethod
    def convert_currency(cls, value: float, from_curr: str, to_curr: str):
        pass

    @staticmethod
    def currency_code_parse(code: str):
        if len(code) != 3:
            raise ValueError("wrong currency code")
        return code.upper()
