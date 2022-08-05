from typing import Any

from money import Money


class Franc(Money):
    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)

    def times(self, multiplier: int) -> Money:
        """
        This method is [exprain]
        docstringの書き方に派閥があるらしい(googleとか
        """
        return Money.franc(self.amount * multiplier)
