from src.abstractions import CurrencyProvider
from datetime import datetime, timedelta
from requests import get


class CurrencyProviderCBR(CurrencyProvider):
    __currency_data = None
    __url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    _last_update_date = datetime.fromtimestamp(0)

    base_curr = 'RUB'
    data_update_interval = timedelta(days=1)
    request_timeout = 3

    @classmethod
    def update_data(cls):
        try:
            cls.__currency_data = get(url=cls.__url, timeout=cls.request_timeout).json
            cls.__last_update_date = datetime.now()
        except Exception as e:
            raise Exception("Currency data update error") from e

    @classmethod
    def get_data(cls):
        if cls.__currency_data is None or (datetime.now() - cls._last_update_date) > cls.data_update_interval:
            cls.update_data()
        return cls.__currency_data

    @classmethod
    def _get_price_base_curr(cls, code: str):
        data = cls.get_data()["Valute"]
        s_nominal = float(data[code]['Nominal'])
        s_value = float(data[code]['Value'])

        return s_value / s_nominal

    @classmethod
    def convert_currency(cls, value: float, from_curr: str, to_curr: str):
        from_curr = cls.currency_code_parse(from_curr)
        to_curr = cls.currency_code_parse(to_curr)

        if from_curr == to_curr:
            return value

        try:
            f_k = 1.0 if from_curr == cls.base_curr else cls._get_price_base_curr(from_curr)
            t_k = 1.0 if to_curr == cls.base_curr else cls._get_price_base_curr(to_curr)

            return (value * f_k)/t_k

        except KeyError:
            raise KeyError("Currency not found")
