import datetime
from dataclasses import dataclass

from investing_pal.finances.currency import Currency
from investing_pal.finances.interest import Interest


@dataclass
class Bond:
    currency: Currency
    face_value: int
    coupon_rate: Interest
    maturity_date: datetime.date
    price: float
    value: float = 0.0

