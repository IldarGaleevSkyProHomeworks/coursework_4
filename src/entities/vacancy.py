from src.abstractions.serializable import Serializable
from src.entities import Currency, MIN_CURRENCY, MAX_CURRENCY


class VacancyAttributes:
    def __init__(self):
        self._data = {}

    def __getitem__(self, name: str):
        if name.lower() in self._data:
            return self._data[name]
        return None

    def __setitem__(self, name: str, value):
        name = name.lower()
        self._data[name] = value

    def __iter__(self):
        return iter(self._data)


class Salary(Serializable):
    def __init__(self, salary_from: Currency = None, salary_to: Currency = None):
        self.__from = salary_from
        self.__to = salary_to

    @property
    def salary_from(self) -> Currency | None:
        return self.__from

    @property
    def salary_to(self) -> Currency | None:
        return self.__to

    def __get_range(self):
        if self.__from is None and self.__to is None:
            return MIN_CURRENCY, MIN_CURRENCY

        low = MIN_CURRENCY if self.__from is None else self.__from
        high = MAX_CURRENCY if self.__to is None else self.__to

        return low, high

    def __lt__(self, other):
        if not issubclass(other.__class__, self.__class__):
            raise TypeError("Can`t compare this objects")

        l1, h1 = self.__get_range()
        l2, h2 = other.__get_range()

        return l1 < l2 or h1 < h2

    def __le__(self, other):
        if not issubclass(other.__class__, self.__class__):
            raise TypeError("Can`t compare this objects")

        l1, h1 = self.__get_range()
        l2, h2 = other.__get_range()

        return l1 <= l2 or h1 <= h2

    def to_dict(self) -> dict:

        return {
            "from": None if self.salary_from is None else self.salary_from.to_dict(),
            "to": None if self.salary_to is None else self.salary_to.to_dict()
        }

    @classmethod
    def from_dict(cls, data: dict) -> any:
        if data is None:
            return None
        return cls(
            salary_from=Currency.from_dict(data.get('from', None)),
            salary_to=Currency.from_dict(data.get('to', None)),
        )


class Vacancy(Serializable):

    def __init__(self, title: str, description: str = None, salary: Salary = None, url: str = None):
        self._salary = salary
        self._description = description
        self._title = title
        self._url = url
        self._attributes = VacancyAttributes()

    def __lt__(self, other):
        if issubclass(other, self.__class__):
            return self.salary < other.salary

    def __le__(self, other):
        if issubclass(other, self.__class__):
            return self.salary <= other.salary

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

    @property
    def attributes(self) -> VacancyAttributes:
        return self._attributes

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
