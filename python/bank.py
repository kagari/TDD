from money import Money
from expression import Expression
from sum import Sum


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(to)
