from typing import Optional


class TestResult:
    def __init__(self) -> None:
        self.runCount = 0

    def testStarted(self) -> None:
        self.runCount += 1

    def summary(self) -> str:
        return f"{self.runCount} run, 0 failed"


class TestCase:
    def __init__(self, name: str) -> None:
        self.name = name

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def run(self) -> TestResult:
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result


class WasRun(TestCase):
    def setUp(self) -> None:
        self.log = "setUp "

    def testMethod(self) -> None:
        self.log += "testMethod "

    def testBrokenMethod(self) -> None:
        raise Exception

    def tearDown(self) -> None:
        self.log += "tearDown "


class TestCaseTest(TestCase):
    def testTemplateMethod(self) -> None:
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown " == test.log

    def testResult(self) -> None:
        test = WasRun("testMethod")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def testFailedResult(self) -> None:
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
# TestCaseTest("testFailedResult").run()
