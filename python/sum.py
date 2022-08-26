from bank import Bank
from money import Money
from expression import Expression


class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression) -> None:
        self.augend: Expression = augend
        self.addend: Expression = addend

    def times(self, multiplier: int) -> Expression:
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def reduce(self, bank: Bank, to: str) -> Money:
        amount: int = self.augend.reduce(bank, to).amount \
          + self.addend.reduce(bank, to).amount
        return Money(amount, to)
