import datetime
import random
from abc import ABC, abstractmethod

from data.value import DataId, Number, Price, Text
from money.currency import PLN


class IDataSource(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name

    @abstractmethod
    def get_number(
        self, data_id: DataId, date: datetime.date | None = None, time: datetime.time | None = None
    ) -> Number:
        pass

    @abstractmethod
    def get_text(self, data_id: DataId, date: datetime.date | None = None, time: datetime.time | None = None) -> Text:
        pass

    @abstractmethod
    def get_price(self, data_id: DataId, date: datetime.date, time: datetime.time | None = None) -> Price:
        pass


class StooqDataSource(IDataSource):
    def __init__(self) -> None:
        super().__init__("stooq")

    def get_number(
        self, data_id: DataId, date: datetime.date | None = None, time: datetime.time | None = None
    ) -> Number:
        assert data_id.source() == self.name
        return Number(data_id=data_id, value=random.randint(1, 100))

    def get_price(self, data_id: DataId, date: datetime.date, time: datetime.time | None = None) -> Price:
        assert data_id.source() == self.name
        return Price(data_id=data_id, value=random.randint(1, 100), currency=PLN)

    def get_text(self, data_id: DataId, date: datetime.date | None = None, time: datetime.time | None = None) -> Text:
        assert data_id.source() == self.name
        return Text(data_id=data_id, value=f"some text {random.randint(1, 100)}")
