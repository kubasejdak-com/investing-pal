from dataclasses import dataclass

from currency import Currency


@dataclass
class Cash:
    currency: Currency
    count: float
