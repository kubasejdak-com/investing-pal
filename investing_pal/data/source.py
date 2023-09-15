import datetime
from abc import ABC, abstractmethod

from data.value import DataId, Number, Price, Text


class IDataSource(ABC):
    @abstractmethod
    def get_number(self, data_id: DataId, date: datetime.date, time: datetime.time | None = None) -> Number:
        pass

    @abstractmethod
    def get_text(self, data_id: DataId, date: datetime.date, time: datetime.time | None = None) -> Text:
        pass

    @abstractmethod
    def get_price(self, data_id: DataId, date: datetime.date, time: datetime.time | None = None) -> Price:
        pass
