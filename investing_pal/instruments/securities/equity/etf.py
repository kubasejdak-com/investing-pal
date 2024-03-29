import datetime
from dataclasses import dataclass
from typing import Optional

from strenum import StrEnum

from instruments.common import IFinancialInstrument
from money.cash import Cash
from money.currency import PLN, Currency


@dataclass
class EtfId:
    isin: str
    ticker: str


class DividendPolicy(StrEnum):
    ACCUMULATING = "accumulating"
    DISTRIBUTING = "distributing"


class Replication(StrEnum):
    PHYSICAL_FULL = "physical (full)"
    PHYSICAL_SAMPLING = "physical (sampling)"
    SYNTHETIC = "synthetic"


@dataclass
class EtfInfo:
    id: EtfId
    name: str
    exchange: str
    issuer: str
    registration_country: str
    currency: Currency
    dividend_policy: DividendPolicy
    hedge: Optional[Currency]
    replication: Replication
    tracked_index: Optional[str]


class Etf(IFinancialInstrument):
    def __init__(self, id: EtfId) -> None:
        super().__init__()
        self._id: EtfId = id

    def price(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        # TODO: implement.
        return Cash(PLN)

    def value(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        return self.price(date, time)
