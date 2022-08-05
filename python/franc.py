from typing import Any

from money import Money


class Franc(Money):
    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)
