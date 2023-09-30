from abc import abstractmethod, ABC


class Serializable(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> any:
        pass
