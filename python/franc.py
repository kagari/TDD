from typing import Any

from money import Money


class Franc(Money):
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> Money:
        """
        This method is [exprain]
        docstringの書き方に派閥があるらしい(googleとか
        """
        return Franc(self.amount * multiplier)