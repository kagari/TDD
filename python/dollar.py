from ast import Str
from typing import Any

from money import Money


class Dollar(Money):
    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)

    def times(self, multiplier: int) -> Money:
        return Money.dollar(self.amount * multiplier)
