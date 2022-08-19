from money import Money
from expression import Expression
from sum import Sum


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        sum_: Sum = source
        return sum_.reduce(to)
