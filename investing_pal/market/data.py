import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass

from investing_pal.finances.currency import Currency


@dataclass
class MarketValue:
    date: datetime.date


@dataclass
class Number(MarketValue):
    value: float

    def __str__(self) -> str:
        return f"{self.date}: {self.value}"


@dataclass
class Text(MarketValue):
    value: str

    def __str__(self) -> str:
        return f"{self.date}: {self.value}"


@dataclass
class Price(Number):
    currency: Currency

    def __str__(self) -> str:
        return f"{self.date}: {self.value} {str(self.currency)}"


@dataclass
class Percentage(Number):
    def __str__(self) -> str:
        return f"{self.date}: {self.value}%"


class IDataSource(ABC):
    @abstractmethod
    def numerical_value(id: str) -> Number:
        pass

    @abstractmethod
    def text_value(id: str) -> Text:
        pass

    @abstractmethod
    def price_value(id: str) -> Price:
        pass

    @abstractmethod
    def percentage_value(id: str) -> Percentage:
        pass
