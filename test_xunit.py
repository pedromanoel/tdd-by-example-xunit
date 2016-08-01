from wasrun import WasRun
from testcase import TestCase

class TestCaseTest(TestCase):
    """Test if the TestCase is working"""

    def test_running(self):
        test = WasRun("test_method")

        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

TestCaseTest("test_running").run()
