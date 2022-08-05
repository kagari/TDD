from __future__ import annotations
from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self) -> None:
        self.amount: int = 0

    def __eq__(self, money: object) -> bool:
        if not isinstance(money, Money):
            return NotImplemented
        return self.amount == money.amount \
           and type(self) == type(money)
    
    @abstractmethod
    def times(self, multiplier: int) -> Money:
        pass

    @staticmethod
    def dollar(amount: int) -> Money:
        from dollar import Dollar
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> Money:
        from franc import Franc
        return Franc(amount)