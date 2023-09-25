from src.providers import CurrencyProviderCBR
from src.entities import Currency
import pytest


@pytest.fixture
def mocked_currency_provider(mocker):
    fake_data = {
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

    mocker.patch("src.providers.currency_provider_cbr.CurrencyProviderCBR.get_data", return_value=fake_data)

    return CurrencyProviderCBR


@pytest.fixture
def mocked_currency():
    Currency.currency_provider = CurrencyProviderCBR
