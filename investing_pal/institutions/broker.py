import datetime
import itertools
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

from institutions.account import Account
from instruments.money.cash import Cash
from investing_pal.instruments.money.cash import Cash
from investing_pal.instruments.money.currency import Currency


class TransactionType(Enum):
    BUY = auto()
    SELL = auto()


@dataclass
class Transaction:
    type: TransactionType
    date: datetime.date
    time: Optional[datetime.time]
    price: Cash
    count: int


class Position:
    def __init__(self) -> None:
        self._transactions: list[Transaction] = []


class Broker:
    pass


class BrokerAccount(Account):
    def __init__(self, currency: Currency = ...) -> None:
        super().__init__(currency)
        self._positions: list[Position] = []

    def value(self) -> Cash:
        return sum([position.value() for position in self._positions])
