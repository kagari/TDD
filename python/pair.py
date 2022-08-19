class Pair:
    def __init__(self, from_: str, to: str) -> None:
        self.__from = from_
        self.__to = to

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Pair):
            return NotImplemented
        return self.__from == __o.__from and self.__to == __o.__to

    def __hash__(self) -> int:
        return 0