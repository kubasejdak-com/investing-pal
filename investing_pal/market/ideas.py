import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

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
    currency: str


aaa = Number(id="security.stock.aapl.nasdaq.name.stooq", date=None, time=None, value="Apple")
bbb = Number(id="security.stock.aapl.nasdaq.price.stooq", date=datetime.date.today(), time=None, value=15.12)
print(aaa)
print(bbb)

# stock id:
#     "security.stock.aapl.nasdaq"
# stock info:
#     "security.stock.aapl.nasdaq.name"
#     "security.stock.aapl.nasdaq.ticker" - included in ID
#     "security.stock.aapl.nasdaq.exchange" - included in ID
#     "security.stock.aapl.nasdaq.currency"


@dataclass
class StockInfo:
    name: str  # Apple
    ticker: str  # aapl
    exchange: str  # NASDAQ
    currency: str  # USD, EUR, PLN


class EtfInfo(StockInfo):
    divident_policy: str  # accumulating/distributing
    replication: str  # physical_sampling, physical, syntetic
    issuer: str  # Vangiard/BlackRock
    registration_country: str  # Ireland/...
    hedge: str  # EUR, USD, PLN, None


class BondInfo(StockInfo):
    face_value: str  # 100 (curreny)
    term: str  # 10y, 2 year
    rate_type: str  # fixed, variable


@dataclass
class BuyTransaction:
    type: str  # buy/sell
    date: datetime.date
    time: Optional[datetime.time]
    price: float
    currency: str
    count: int


class IInfoSource:
    def get_stock_info(self, id: DataId) -> StockInfo:
        pass

    def get_etf_info(self, id: DataId) -> EtfInfo:
        pass

    def get_bond_info(seld, id: DataId) -> BondInfo:
        pass


class IDataSource:
    pass
