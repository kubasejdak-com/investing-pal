from abc import ABC, abstractmethod

from money.cash import Cash
from money.currency import PLN, Currency


class Account(ABC):
    def __init__(self, name: str, currency: Currency = PLN, currency_conversion: bool = False) -> None:
        self._name: str = name
        self._currency = currency
        self._currency_conversion = currency_conversion
        self._cash: Cash = Cash(currency, 0.0)

    def name(self) -> str:
        return self._name

    def depose_cash(self, cash: Cash) -> None:
        # TODO: implement.
        pass

    def withdraw_cash(self, count: float) -> Cash:
        # TODO: implement.
        pass

    def cash_balance(self) -> Cash:
        return self._cash

    @abstractmethod
    def value(self) -> Cash:
        pass

    @abstractmethod
    def convert_currency(self, cash: Cash) -> Cash:
        pass
