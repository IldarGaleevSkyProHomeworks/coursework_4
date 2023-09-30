from src.abstractions.serializable import Serializable
from src.entities.salary import Salary


class Vacancy(Serializable):

    def __init__(self, title: str, description: str = None, salary: Salary = None, url: str = None):
        self._salary = salary
        self._description = description
        self._title = title
        self._url = url

    def __eq__(self, other):
        if issubclass(other.__class__, self.__class__):
            return (self.title == other.title and
                    self.url == other.url and
                    self.description == other.description and
                    self.salary == other.salary)
        return False

    def __lt__(self, other):
        if self.salary is None:
            return True
        if issubclass(other.__class__, self.__class__):
            return self.salary < other.salary

    def __le__(self, other):
        if self.salary is None:
            return True
        if issubclass(other.__class__, self.__class__):
            return self.salary <= other.salary

    def __str__(self):

        if self.salary is not None:
            s = str(self.salary)
            s = f' Зарплата: {s if s else "Не указано"}'
        else:
            s = ''
        return f'{self.title}{s}'

    @property
    def salary(self) -> Salary | None:
        return self._salary

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    @property
    def url(self):
        return self._url

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "salary": None if self.salary is None else self.salary.to_dict(),
            "url": self.url
        }

    @classmethod
    def from_dict(cls, data: dict) -> any:
        if data is None:
            return None

        return cls(
            title=data.get('title', None),
            description=data.get('description', None),
            url=data.get('url', None),
            salary=Salary.from_dict(data.get('salary', None))
        )
