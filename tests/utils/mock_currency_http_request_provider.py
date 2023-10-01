from src.abstractions import HttpRequestProvider


class MockCurrencyHttpRequestProvider(HttpRequestProvider):
    @classmethod
    def get_data_dict(cls, url, **kwargs):
        return {
            "Valute": {
                "CU1": {
                    "Nominal": 1,
                    "Value": 2
                },
                "CU2": {
                    "Nominal": 6,
                    "Value": 24
                },
                "CU3": {
                    "Nominal": 1,
                    "Value": 8
                }
            }
        }
