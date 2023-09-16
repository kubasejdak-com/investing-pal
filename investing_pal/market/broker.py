from abc import ABC, abstractmethod

from instruments.common import InstrumentId
from market.account import Account, AccountInfo
from market.institution import IInstitution
from market.transaction import Transaction
from money.cash import Cash
from money.currency import PLN


class Position:
    def __init__(self) -> None:
        self._transactions: list[Transaction] = []


class BrokerAccount(Account):
    def __init__(self, name: str, info: AccountInfo) -> None:
        super().__init__(name, info)
        self._positions: list[Position] = []

    def value(self) -> Cash:
        # return sum([position.value() for position in self._positions])
        # TODO: implement.
        return Cash(PLN)

    @abstractmethod
    def buy_instrument(self, instrument_id: InstrumentId, count: float) -> None:
        pass

    @abstractmethod
    def sell_instrument(self, instrument_id: InstrumentId, count: float) -> None:
        pass


class Broker(IInstitution):
    pass
