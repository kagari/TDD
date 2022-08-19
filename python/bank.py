from money import Money
from expression import Expression
from sum import Sum


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        if issubclass(Money, type(source)):
            return source
        sum_: Sum = source
        return sum_.reduce(to)
