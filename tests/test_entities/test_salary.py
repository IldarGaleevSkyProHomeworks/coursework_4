from src.entities import Currency
from src.entities import Salary


def test_salary_compare(mocked_currency):
    salary1 = Salary(
        salary_from=Currency(1, 'RUB'),
        salary_to=Currency(2, 'RUB')
    )

    salary2 = Salary(
        salary_from=Currency(2, 'RUB'),
        salary_to=Currency(3, 'RUB')
    )

    salary3 = Salary()

    assert salary1 < salary2
    assert salary1 <= salary2
    assert salary3 < salary1
    assert salary3 < salary2


def test_serialize(mocked_currency):
    salary = Salary(
        salary_from=Currency(1, 'RUB'),
    )

    assert salary.to_dict() == {'from': {'currency': 'RUB', 'value': 1.0}, 'to': None}


def test_deserialize(mocked_currency):
    salary = Salary.from_dict({'from': {'currency': 'RUB', 'value': 1.0}})
    assert salary.salary_from.value == 1
    assert salary.salary_from.code == 'RUB'
    assert salary.salary_to is None
