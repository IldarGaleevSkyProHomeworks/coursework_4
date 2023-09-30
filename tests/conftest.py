import os.path

from src.providers import CurrencyProviderCBR, VacancyProviderHeadHunter
from src.entities import Currency
import pytest

from tests.utils.mock_currency_http_request_provider import MockCurrencyHttpRequestProvider
from tests.utils.mock_vacancy_provider_hh import MockVacancyProviderHeadHunter

TEST_DATA_DIR = os.path.join('tests', 'data')


@pytest.fixture
def mocked_currency_provider():
    default_provider = CurrencyProviderCBR.http_request_provider
    CurrencyProviderCBR.http_request_provider = MockCurrencyHttpRequestProvider

    yield CurrencyProviderCBR

    CurrencyProviderCBR.http_request_provider = default_provider


@pytest.fixture
def mocked_currency(mocked_currency_provider):
    default_currency_provider = Currency.currency_provider
    Currency.currency_provider = CurrencyProviderCBR

    yield Currency

    Currency.currency_provider = default_currency_provider


@pytest.fixture
def mocked_vacancy_provider_head_hunter():
    default_provider = VacancyProviderHeadHunter.http_request_provider
    MockVacancyProviderHeadHunter.test_data_dir = TEST_DATA_DIR
    VacancyProviderHeadHunter.http_request_provider = MockVacancyProviderHeadHunter

    yield VacancyProviderHeadHunter

    VacancyProviderHeadHunter.http_request_provider = default_provider
