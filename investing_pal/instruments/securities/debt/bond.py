import datetime
from dataclasses import dataclass
from enum import Enum, auto

from investing_pal.instruments.instrument import IFinancialInstrument
from investing_pal.instruments.money.cash import Cash
from investing_pal.instruments.money.currency import Currency


@dataclass
class BondId:
    id: str


class RateType(Enum):
    FIXED = auto()
    VARIABLE = auto()


@dataclass
class BondInfo:
    id: BondId
    name: str
    exchange: str
    face_value: str  # 100 (curreny)
    term: str  # 10y, 2 year
    rate_type: RateType


class Bond(IFinancialInstrument):
    def __init__(self, id: BondId) -> None:
        super().__init__()
        self._id: BondId = id

    def price(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        pass

    def value(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        pass
