from abc import ABC, abstractmethod

from instruments.money.cash import Cash
from instruments.money.currency import PLN, Currency


class Account(ABC):
    def __init__(self, currency: Currency = PLN) -> None:
        self._cash: Cash = Cash()

    @abstractmethod
    def value(self) -> Cash:
        pass
