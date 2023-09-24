import datetime
from dataclasses import dataclass

from data.value import DataId
from instruments.common import IFinancialInstrument
from money.cash import Cash
from money.currency import PLN, Currency


@dataclass
class StockId(DataId):
    ticker: str
    exchange_id: str

    @staticmethod
    def uid_format() -> str:
        return "instrument.stock.{ticker}.{exchange_id}"

    def uid(self) -> str:
        return self.uid_format().format(ticker=self.ticker.replace(".", ":::"), exchange_id=self.exchange_id)


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
