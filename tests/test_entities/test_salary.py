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
