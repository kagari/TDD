from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def reduce(to: str) -> 'Money':
        pass
