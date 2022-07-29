class Money:
    def __init__(self) -> Money:
        self.amount: int = 0

    def equals(money: Money) -> bool:
        return self.amount == money.amount