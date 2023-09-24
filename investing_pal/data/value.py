import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional

from money.currency import Currency


class DataId(ABC):
    @staticmethod
    @abstractmethod
    def uid_format() -> str:
        pass

    @abstractmethod
    def uid(self) -> str:
        pass

    def source(self) -> str:
        return self.uid().split("@")[0]

    def __str__(self) -> str:
        return self.uid()


class DataType(Enum):
    NUMBER = auto()
    PRICE = auto()
    TEXT = auto()


@dataclass(kw_only=True)
class MarketData:
    type: DataType = field(init=False)
    data_id: DataId
    date: datetime.date | None = None
    time: datetime.time | None = None


@dataclass
class Number(MarketData):
    value: float

    def __post_init__(self):
        self.type = DataType.NUMBER


@dataclass
class Price(Number):
    currency: Currency

    def __post_init__(self):
        self.type = DataType.PRICE


@dataclass
class Text(MarketData):
    value: str

    def __post_init__(self):
        self.type = DataType.TEXT
