from money import Money
from expression import Expression
from pair import Pair

class Bank:
    def __init__(self) -> None:
        self.rates: dict[Pair, int] = dict()

    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)

    def add_rate(self, from_: str, to: str, rate: int) -> None:
        self.rates[Pair(from_, to)] = rate

    def rate(self, from_: str, to: str) -> int:
        if from_ == to:
            return 1
        return self.rates[Pair(from_, to)]