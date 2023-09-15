import datetime
from dataclasses import dataclass

from strenum import StrEnum

from instruments.common import IFinancialInstrument
from money.cash import Cash
from money.currency import PLN, Currency


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
        # TODO: implement.
        return Cash(PLN)

    def value(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        # TODO: implement.
        return Cash(PLN)
