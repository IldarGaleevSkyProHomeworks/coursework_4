from abc import abstractmethod, ABC

from src.abstractions import Serializable
from src.entities.vacancy import Vacancy


class VacancySerializer(ABC):
    @classmethod
    @abstractmethod
    def load_list_from_file(cls, file_name: str, encoding: str = 'UTF-8', **kwargs) -> list[Vacancy]:
        pass

    @classmethod
    @abstractmethod
    def save_list_to_file(cls, data: list[Vacancy], file_name: str, encoding: str = 'UTF-8', **kwargs):
        pass
