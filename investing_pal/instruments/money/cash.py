from dataclasses import dataclass

from instruments.money.currency import Currency


@dataclass
class Cash:
    currency: Currency
    count: float
