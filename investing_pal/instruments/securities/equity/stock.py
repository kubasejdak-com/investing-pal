import datetime
from dataclasses import dataclass

from instrument import IFinancialInstrument
from money.cash import Cash
from money.currency import Currency


@dataclass
class StockId:
    isin: str
    ticker: str


@dataclass
class StockInfo:
    id: StockId
    name: str
    exchange: str
    currency: Currency


class Stock(IFinancialInstrument):
    def __init__(self, id: StockId) -> None:
        super().__init__()
        self._id: StockId = id

    def price(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        pass

    def value(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        pass
