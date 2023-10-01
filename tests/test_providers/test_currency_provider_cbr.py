import pytest


def test_convert_currency(mocked_currency_provider):
    with pytest.raises(ValueError):
        _ = mocked_currency_provider.convert_currency(0, 'CURRENCY', 'cur')

    with pytest.raises(KeyError):
        _ = mocked_currency_provider.convert_currency(0, 'cu1', 'cur')

    assert mocked_currency_provider.convert_currency(123.45, 'CUR', 'cur') == 123.45

    assert mocked_currency_provider.convert_currency(1, 'CU1', mocked_currency_provider.base_curr) == 2
    assert mocked_currency_provider.convert_currency(2, mocked_currency_provider.base_curr, 'CU1') == 1
    assert mocked_currency_provider.convert_currency(1, 'CU1', 'CU2') == 0.5
