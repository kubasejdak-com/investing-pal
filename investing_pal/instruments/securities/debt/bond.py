import datetime
from dataclasses import dataclass

from strenum import StrEnum

from instruments.instrument import IFinancialInstrument
from instruments.money.cash import Cash
from instruments.money.currency import Currency


@dataclass
class BondId:
    id: str


class RateType(StrEnum):
    FIXED = "fixed"
    VARIABLE = "variable"


@dataclass
class BondInfo:
    id: BondId
    name: str
    exchange: str
    currency: Currency
    face_value: Cash
    term: datetime.timedelta
    rate_type: RateType


class Bond(IFinancialInstrument):
    def __init__(self, id: BondId) -> None:
        super().__init__()
        self._id: BondId = id

    def price(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        pass

    def value(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        pass
