import datetime
from dataclasses import dataclass

from investing_pal.finances.currency import Currency


@dataclass
class Bond:
    nominal_value: int
    currency: Currency
    coupon: float
    maturity: datetime.date
