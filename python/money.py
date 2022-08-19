from __future__ import annotations
from typing import TYPE_CHECKING

from expression import Expression
if TYPE_CHECKING:
    from sum import Sum


class Money(Expression):
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __eq__(self, money: object) -> bool:
        if not isinstance(money, Money):
            return NotImplemented
        return self.amount == money.amount \
           and self.get_currency() == money.get_currency()
    
    def times(self, multiplier: int) -> Money:
        return Money(self.amount * multiplier, self.currency)

    def get_currency(self) -> str:
        return self.currency

    def __str__(self) -> str:
        return f"{self.amount}{self.currency}"

    def plus(self, addend: Money) -> Sum:
        from sum import Sum
        return Sum(self, addend)

    def reduce(self, to: str) -> Money:
        return self

    @staticmethod
    def dollar(amount: int) -> Money:
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount: int) -> Money:
        return Money(amount, 'CHF')
