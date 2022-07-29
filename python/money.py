from typing import Any


class Money:
    def __init__(self) -> Any:
        self.amount: int = 0

    def __eq__(self, money: Any) -> bool:
        return self.amount == money.amount \
           and type(self) == type(money)