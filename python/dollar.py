class Dollar(Money):
    def __init__(self, amount: int) -> Dollar:
        self.amount = amount

    def times(self, multiplier: int) -> Dollar:
        return Dollar(self.amount * multiplier)