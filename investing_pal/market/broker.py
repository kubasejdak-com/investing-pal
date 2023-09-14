from market.account import Account
from market.transaction import Transaction
from money.cash import Cash
from money.currency import Currency


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
