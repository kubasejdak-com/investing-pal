import datetime
from dataclasses import dataclass

from data.ids import DataId, DataType
from instruments.common import IFinancialInstrument
from money.cash import Cash
from money.currency import PLN, Currency


@dataclass
class StockId(DataId):
    ticker: str
    exchange: str

    def _inner_type(self) -> DataType:
        return DataType.INSTRUMENT_STOCK

    def _inner_uid(self) -> str:
        return f"{self.ticker.replace('.', ':')}.{self.exchange}"


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
