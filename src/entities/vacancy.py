from src.entities import Currency


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


class Vacancy:

    def __init__(self, title: str, description: str = None, salary: Currency = None, url: str = None):
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
    def salary(self) -> Currency | None:
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
