from datetime import datetime

from src.abstractions import SearchResult
from src.entities import Vacancy
from src.providers import VacancyProviderHeadHunter, VacancyProviderSuperjob
from src.providers.vacancy_composer import VacancyComposer
from src.serializers import JsonVacancySerializer


def get_vacancy_list(data: dict[str, SearchResult], sort: bool = True) -> list[Vacancy]:
    sorted_vacancies = []
    for s_result in data.values():
        sorted_vacancies.extend(s_result.result_list)

    if sort:
        return sorted(sorted_vacancies, reverse=True)

    return sorted_vacancies


def print_table(data: dict[str, SearchResult], top_count=None):
    if not data:
        print("Нет результатов!")
        return

    vacancy_list = get_vacancy_list(data)
    vacancy_list = vacancy_list[:top_count] if top_count else vacancy_list

    col_size = [
        max([len(v.title) for v in vacancy_list]),
        15,
        15
    ]

    # == Statistic ==
    max_name_len = max([len(n) for n in data.keys()])
    total = 0
    stat = ''
    for name, res in data.items():
        total += res.total_results
        stat += f'{name: >{max_name_len}}: {res.total_results} - {res.total_pages} страниц\n'

    stat += f'{"Всего": >{max_name_len}}: {total}\n'

    # == Table header ==
    h_line = '-' * (col_size[0] + col_size[1] + col_size[2] + 4) + '\n'

    result = ''
    result += f'{"Title": >{col_size[0]}} | {"Salary from": <{col_size[1]}} | {"Salary to": <{col_size[2]}}\n'
    result += h_line

    # == Table rows ==

    for vacancy in vacancy_list:
        result += (f'{vacancy.title: >{col_size[0]}} | '
                   f'{"-" if vacancy.salary is None or vacancy.salary.salary_from is None else str(vacancy.salary.salary_from): <{col_size[1]}} | '
                   f'{"-" if vacancy.salary is None or vacancy.salary.salary_to is None else str(vacancy.salary.salary_to): <{col_size[2]}}'
                   f'\n')
    result += h_line + '\n'

    # print(stat + result)
    print(result + stat)


def search_vacancy(composer: VacancyComposer):
    def get_input(prompt: str) -> str:
        r = input(prompt + '\n(оставьте пустым по-умолчанию)> ')
        print()
        return r

    def get_int(prompt: str) -> int | None:
        input_str = get_input(prompt)
        if input_str and input_str.isdigit():
            return int(input_str)

        return None

    def get_list(prompt: str) -> list | None:
        input_str = get_input(prompt)
        if input_str:
            return input_str.split(',')

        return None

    keyword = input("Введите ключевые слова для поиска\n> ")

    providers = get_list(f"Укажите провайдеров через запятую: {', '.join(composer.provider_names)}")
    per_page = get_int("Укажите максимальное число вакансий на странице")
    page_num = get_int("Укажите страницу")
    top_count = get_int("Число выводимых результатов")

    search_result_list = composer.get_vacancies(
        search_text=keyword,
        per_page=per_page,
        page_num=page_num,
        providers=providers)

    print_table(
        search_result_list,
        top_count=top_count
    )
    return search_result_list


def save_to_file(data: dict[str, SearchResult]):
    while True:
        try:
            file_name_default = f"vacancy_{datetime.now().strftime('%d%m%Y%H%M%S')}.json"
            file_name = input(f"Имя файла [{file_name_default}]: ")
            if not file_name:
                file_name = file_name_default

            JsonVacancySerializer.save_list_to_file(get_vacancy_list(data), file_name)
            break
        except KeyboardInterrupt:
            print("Файл не сохранен")
            break
        except Exception as ex:
            print(f"Не удалось сохранить файл: {ex}")


def user_interaction(vacancy_composer: VacancyComposer):
    result = []
    while True:
        try:
            result = search_vacancy(vacancy_composer)
        except KeyboardInterrupt:
            if result and input("Сохранить результаты в файл? y/n (n):").lower() == 'y':
                save_to_file(result)
            break


if __name__ == '__main__':
    user_interaction(
        VacancyComposer(
            [
                VacancyProviderHeadHunter(),
                VacancyProviderSuperjob()
            ]
        )
    )
