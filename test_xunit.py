from wasrun import WasRun
from testcase import TestCase

class TestCaseTest(TestCase):
    """Test if the TestCase is working"""

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert(test.log == "setup test_method tear_down ")

    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

TestCaseTest("test_template_method").run()
TestCaseTest("test_result").run()
