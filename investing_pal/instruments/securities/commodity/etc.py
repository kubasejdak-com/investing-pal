import datetime
from dataclasses import dataclass

from investing_pal.instruments.instrument import IFinancialInstrument
from investing_pal.instruments.money.cash import Cash
from investing_pal.instruments.money.currency import Currency


@dataclass
class EtcId:
    isin: str
    ticker: str


@dataclass
class EtcInfo:
    id: EtcId
    name: str
    exchange: str
    currency: Currency


class Etc(IFinancialInstrument):
    def __init__(self, id: EtcId) -> None:
        super().__init__()
        self._id: EtcId = id

    def price(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        pass

    def value(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        pass