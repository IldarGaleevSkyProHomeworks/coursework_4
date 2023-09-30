from src.abstractions.vacancy_serializer import VacancySerializer
from json import dump, load

from src.entities import Vacancy


class JsonVacancySerializer(VacancySerializer):
    @classmethod
    def load_list_from_file(cls, file_name: str, encoding: str = 'UTF-8', **kwargs) -> list[Vacancy]:
        with open(file_name, 'r', encoding=encoding) as file:
            return [Vacancy.from_dict(item) for item in load(file, **kwargs)]

    @classmethod
    def save_list_to_file(cls, data: list[Vacancy], file_name: str, encoding: str = 'UTF-8', **kwargs):
        data_list = [item.to_dict() for item in data]
        with open(file_name, 'w', encoding=encoding) as file:
            dump(data_list, file, **kwargs)

