from dataclasses import dataclass


@dataclass
class Currency:
    name: str
    code: str

USD = Currency("US dollar", "USD")
PLN = Currency("Polish zloty", "PLN")