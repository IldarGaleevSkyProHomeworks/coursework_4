from src.providers import CurrencyProviderCBR
from src.entities import Currency
import pytest

from tests.utils.mock_currency_http_request_provider import MockCurrencyHttpRequestProvider


@pytest.fixture
def mocked_currency_provider():
    default_provider = CurrencyProviderCBR.http_request_provider
    CurrencyProviderCBR.http_request_provider = MockCurrencyHttpRequestProvider

    yield CurrencyProviderCBR

    CurrencyProviderCBR.http_request_provider = default_provider


@pytest.fixture
def mocked_currency():
    Currency.currency_provider = CurrencyProviderCBR
