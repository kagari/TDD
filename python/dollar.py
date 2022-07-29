from typing import Any

from money import Money


class Dollar(Money):
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> Money:
        return Dollar(self.amount * multiplier)