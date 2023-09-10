from dataclasses import dataclass

from investing_pal.instruments.money.currency import Currency


@dataclass
class Cash:
    currency: Currency
    count: float
