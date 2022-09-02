from typing import Optional


class WasRun:
    def __init__(self, name: str) -> None:
        self.wasRun: Optional[int] = None

    def run(self) -> None:
        self.testMethod()

    def testMethod(self) -> None:
        self.wasRun = 1


test =  WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
