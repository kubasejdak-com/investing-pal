import datetime
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

from money.cash import Cash


class TransactionType(Enum):
    BUY = auto()
    SELL = auto()


@dataclass
class Transaction:
    type: TransactionType
    date: datetime.date
    time: Optional[datetime.time]
    price: Cash
    count: int
