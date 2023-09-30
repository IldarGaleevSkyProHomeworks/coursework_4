import pprint

from src.providers import VacancyProviderHeadHunter, VacancyProviderSuperjob, CurrencyProviderCBR
from src.entities import Currency, Vacancy


def print_table(data: list[Vacancy], col_size=None):
    if col_size is None:
        col_size = [100, 15, 15]
    result = ''
    result += f'{"Title": >{col_size[0]}} | {"Salary from": <{col_size[1]}} | {"Salary to": <{col_size[2]}}\n'
    result += '-' * (col_size[0] + col_size[1] + col_size[2] + 4) + '\n'
    for vacancy in data:
        result += (f'{vacancy.title: >{col_size[0]}} | '
                   f'{"-" if vacancy.salary is None or vacancy.salary.salary_from is None else str(vacancy.salary.salary_from): <{col_size[1]}} | '
                   f'{"-" if vacancy.salary is None or vacancy.salary.salary_to is None else str(vacancy.salary.salary_to): <{col_size[2]}}'
                   f'\n')
    print(result)


if __name__ == '__main__':

    Currency.currency_provider = CurrencyProviderCBR

    providers = [
        VacancyProviderHeadHunter(),
        VacancyProviderSuperjob()
    ]

    res = []
    for provider in providers:
        res.extend(provider.get_vacancies(search_text='python').result_list)

    res = sorted(res, reverse=True)
    print_table(res)

    # pprint.pprint([str(vac) for vac in res])
