from wasrun import WasRun
from testcase import TestCase

class TestCaseTest(TestCase):
    """Test if the TestCase is working"""

    def test_running(self):
        test = WasRun("test_method")

        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

    def test_setup(self):
        test = WasRun("test_method")
        test.run()
        assert(test.wasSetUp)

TestCaseTest("test_running").run()
TestCaseTest("test_setup").run()
