from typing import Optional


class TestCase:
    def __init__(self, name: str) -> None:
        self.name = name

    def run(self) -> None:
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name: str) -> None:
        self.wasRun: Optional[int] = None
        super().__init__(name)

    def testMethod(self) -> None:
        self.wasRun = 1


test =  WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
