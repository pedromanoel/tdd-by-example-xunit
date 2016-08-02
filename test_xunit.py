from wasrun import WasRun
from testcase import TestCase

class TestCaseTest(TestCase):
    """Test if the TestCase is working"""

    def setup(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert(self.test.wasRun)

    def test_setup(self):
        self.test.run()
        assert(self.test.wasSetUp)

TestCaseTest("test_running").run()
TestCaseTest("test_setup").run()
