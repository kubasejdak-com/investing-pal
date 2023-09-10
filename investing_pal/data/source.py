import datetime
from abc import ABC, abstractmethod

from investing_pal.data.value import DataId, Number, Price, Text


class IDataSource(ABC):
    @abstractmethod
    def get_number(self, id: DataId, date: datetime.date, time: datetime.time | None = None) -> Number:
        pass

    @abstractmethod
    def get_text(self, id: DataId, date: datetime.date, time: datetime.time | None = None) -> Text:
        pass

    @abstractmethod
    def get_price(seld, id: DataId, date: datetime.date, time: datetime.time | None = None) -> Price:
        pass
