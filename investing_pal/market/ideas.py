import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class Transaction:
    type: str  # buy/sell
    date: datetime.date
    time: Optional[datetime.time]
    price: float
    currency: str
    count: int
