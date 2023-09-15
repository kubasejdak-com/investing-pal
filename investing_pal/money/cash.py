from dataclasses import dataclass

from money.currency import Currency


@dataclass
class Cash:
    currency: Currency
    count: float = 0.0
