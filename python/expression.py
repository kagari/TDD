from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bank import Bank
    from money import Money


class Expression(ABC):
    @abstractmethod
    def times(self, multiplier: int) -> Expression:
        pass

    @abstractmethod
    def plus(self, addend: Expression) -> Expression:
        pass

    @abstractmethod
    def reduce(self, bank: Bank, to: str) -> Money:
        pass
