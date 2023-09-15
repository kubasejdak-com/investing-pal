import datetime
from dataclasses import dataclass
from typing import Optional

from money.currency import Currency

DataId = str


@dataclass
class MarketData:
    id: DataId
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
