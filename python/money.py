from __future__ import annotations
from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __eq__(self, money: object) -> bool:
        if not isinstance(money, Money):
            return NotImplemented
        return self.amount == money.amount \
           and type(self) == type(money)
    
    @abstractmethod
    def times(self, multiplier: int) -> Money:
        pass

    def get_currency(self) -> str:
        return self.currency

    @staticmethod
    def dollar(amount: int) -> Money:
        from dollar import Dollar
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount: int) -> Money:
        from franc import Franc
        return Franc(amount, 'CHF')
