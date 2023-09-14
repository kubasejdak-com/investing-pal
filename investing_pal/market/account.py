from abc import ABC, abstractmethod

from instruments.money.cash import Cash
from instruments.money.currency import PLN, Currency


class Account(ABC):
    def __init__(self, name: str, currency: Currency = PLN) -> None:
        self._name: str = name
        self._cash: Cash = Cash()

    def name(self) -> str:
        return self._name

    def balance(self) -> Cash:
        return self._cash

    @abstractmethod
    def value(self) -> Cash:
        pass
