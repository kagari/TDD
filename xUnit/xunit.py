class WasRun:
    def __init__(self, name: str) -> None:
        self.wasRun = None

    def testMethod(self) -> None:
        self.wasRun = 1


test =  WasRun("testMethod")
print(test.wasRun)
test.testMethod()
print(test.wasRun)
