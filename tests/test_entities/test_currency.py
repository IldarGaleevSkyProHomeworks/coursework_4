import pytest

from src.entities import Currency


@pytest.fixture
def currency_fixture(mocked_currency_provider, mocked_currency):
    return Currency(2, 'cu1')


def test_currency_value(currency_fixture):
    assert currency_fixture.value == 2


def test_currency_code(currency_fixture):
    assert currency_fixture.code == 'CU1'


def test_currency_get_item(currency_fixture):
    assert currency_fixture['CU1'] == 2
    assert currency_fixture['CU2'] == 1


def test_unassigned_currency_provider(currency_fixture):
    currency_fixture.currency_provider = None
    with pytest.raises(ReferenceError):
        _ = currency_fixture['cu1']


def test_currency_compare(mocked_currency_provider, mocked_currency):
    currency1 = Currency(2, 'cu1')
    currency2 = Currency(1, 'cu2')
    currency3 = Currency(1, 'cu1')

    assert currency1 == currency2
    assert currency1 > currency3
    assert currency1 <= currency2
    assert currency1 != 2

    with pytest.raises(TypeError):
        _ = 2 > currency1

    with pytest.raises(TypeError):
        _ = 2 >= currency1
