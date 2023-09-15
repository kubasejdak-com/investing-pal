import datetime
from dataclasses import dataclass
from typing import Optional

from money.currency import Currency

DataId = str

# instrument.[stock|etf|etc].<ticker>.<source>
# instrument.[bond].<symbol>.<source>
# source.<source>
# economy.inflation.<

# economy.inflation.poland.yoy.nbp


@dataclass
class MarketData:
    data_id: DataId
    date: Optional[datetime.date]
    time: Optional[datetime.time]


@dataclass
class Number(MarketData):
    value: float


@dataclass
class Text(MarketData):
    value: str


@dataclass
class Price(Number):
    currency: Currency
