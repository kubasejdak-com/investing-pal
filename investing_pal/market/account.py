from abc import ABC, abstractmethod
from dataclasses import dataclass

from money.cash import Cash
from money.currency import PLN, Currency


@dataclass
class AccountInfo:
    type: str
    currency: Currency = PLN
    currency_conversion: bool = False


class Account(ABC):
    def __init__(self, name: str, info: AccountInfo) -> None:
        self._name: str = name
        self._info: AccountInfo = info
        self._cash: Cash = Cash(info.currency)

    def name(self) -> str:
        return self._name

    def depose_cash(self, cash: Cash) -> None:
        # TODO: implement.
        pass

    def withdraw_cash(self, count: float) -> Cash:
        # TODO: implement.
        return Cash(PLN)

    def cash_balance(self) -> Cash:
        return self._cash

    @abstractmethod
    def value(self) -> Cash:
        pass

    @abstractmethod
    def convert_currency(self, cash: Cash) -> Cash:
        pass
