import datetime
from dataclasses import dataclass

from investing_pal.instruments.instrument import IFinancialInstrument
from investing_pal.instruments.money.cash import Cash
from investing_pal.instruments.money.currency import Currency


@dataclass
class EtfId:
    isin: str
    ticker: str


@dataclass
class EtfInfo:
    id: EtfId
    name: str
    exchange: str
    currency: Currency


class Etf(IFinancialInstrument):
    def __init__(self, id: EtfId) -> None:
        super().__init__()
        self._id: EtfId = id

    def price(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        pass

    def value(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        pass
