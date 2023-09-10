import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


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
