from typing import Optional


class TestCase:
    def __init__(self, name: str) -> None:
        self.name = name

    def setUp(self):
        pass

    def run(self) -> None:
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def setUp(self):
        self.wasRun: Optional[int] = 1
        self.wasSetUp = 1

    def testMethod(self) -> None:
        self.wasRun = 1


class TestCaseTest(TestCase):
    def testRunning(self) -> None:
        test =  WasRun("testMethod")
        test.run()
        assert test.wasRun

    def testSetUp(self):
        test =  WasRun("testMethod")
        test.run()
        assert test.wasSetUp


TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
