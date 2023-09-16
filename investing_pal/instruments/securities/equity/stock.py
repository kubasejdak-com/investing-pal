import datetime
from dataclasses import dataclass

from data.ids import DataId, DataType
from instruments.common import IFinancialInstrument
from money.cash import Cash
from money.currency import PLN, Currency


class StockId(DataId):
    def __init__(self, ticker: str, exchange: str) -> None:
        super().__init__(DataType.INSTRUMENT_STOCK)
        self.ticker: str = ticker
        self.exchange: str = exchange

    def __str__(self) -> str:
        data_id = super().__str__()
        return f"{data_id}.{self.ticker}:{self.exchange}"


@dataclass
class StockInfo:
    id: StockId
    name: str
    isin: str
    currency: Currency


class Stock(IFinancialInstrument):
    def __init__(self, id: StockId) -> None:
        super().__init__()
        self._id: StockId = id

    def price(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        # TODO: implement.
        return Cash(PLN)

    def value(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        # TODO: implement.
        return Cash(PLN)
