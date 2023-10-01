from abc import abstractmethod, ABC


class Serializable(ABC):
    """
    Can be converted from/to dict
    """
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> any:
        pass
