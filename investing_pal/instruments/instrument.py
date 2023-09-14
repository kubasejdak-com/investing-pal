import datetime
from abc import ABC, abstractmethod

from money.cash import Cash


class IFinancialInstrument(ABC):
    @abstractmethod
    def price(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        pass

    @abstractmethod
    def value(self, date: datetime.date, time: datetime.time | None = None) -> Cash:
        pass
