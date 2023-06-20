from abc import ABC, abstractmethod


class Interest(ABC):
    @abstractmethod
    def rate() -> float:
        pass


class FixedInterest(Interest):
    def __init__(self, rate: float) -> None:
        super().__init__()
        self._rate: float = rate

    def rate(self) -> float:
        return self._rate


class VariableInterest(Interest):
    pass
