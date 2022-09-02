from typing import Optional


class TestCase:
    def __init__(self, name: str) -> None:
        self.name = name

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def run(self) -> None:
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()


class WasRun(TestCase):
    def setUp(self) -> None:
        self.log = "setUp "

    def testMethod(self) -> None:
        self.log = self.log + "testMethod "

    def tearDown(self) -> None:
        self.log = self.log + "tearDown "


class TestCaseTest(TestCase):
    def testTemplateMethod(self) -> None:
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown " == test.log

TestCaseTest("testTemplateMethod").run()
