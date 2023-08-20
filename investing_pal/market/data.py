import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass

from investing_pal.finances.currency import Currency


@dataclass
class MarketValue:
    date: datetime.date


@dataclass
class NumericalValue(MarketValue):
    value: float

    def __str__(self) -> str:
        return f"{self.date}: {self.value}"


@dataclass
class TextValue(MarketValue):
    value: str

    def __str__(self) -> str:
        return f"{self.date}: {self.value}"


@dataclass
class PriceValue(NumericalValue):
    currency: Currency

    def __str__(self) -> str:
        return f"{self.date}: {self.value} {str(self.currency)}"


@dataclass
class PercentageValue(NumericalValue):
    def __str__(self) -> str:
        return f"{self.date}: {self.value}%"


class IDataSource(ABC):
    @abstractmethod
    def numerical_value(id: str) -> NumericalValue:
        pass

    @abstractmethod
    def text_value(id: str) -> TextValue:
        pass

    @abstractmethod
    def price_value(id: str) -> PriceValue:
        pass

    @abstractmethod
    def percentage_value(id: str) -> PercentageValue:
        pass
