from dataclasses import dataclass


@dataclass
class Currency:
    name: str
    code: str

    def __str__(self) -> str:
        return self.code


USD = Currency("US dollar", "USD")
PLN = Currency("Polish zloty", "PLN")
