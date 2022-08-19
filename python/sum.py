from money import Money
from expression import Expression


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money) -> None:
        self.augend: Money = augend
        self.addend: Money = addend

    def reduce(self, to: str) -> Money:
        amount: int = self.augend.amount + self.addend.amount
        return Money(amount, to)
