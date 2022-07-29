from typing import Any

from money import Money


class Dollar(Money):
    def __init__(self, amount: int) -> Any:
        self.amount = amount

    def times(self, multiplier: int) -> Any:
        return Dollar(self.amount * multiplier)