from wasrun import WasRun
from testcase import TestCase, TestResult

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

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

    def test_result_formatting(self):
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert("1 run, 1 failed" == result.summary())

TestCaseTest("test_template_method").run()
TestCaseTest("test_result").run()
TestCaseTest("test_result_formatting").run()
TestCaseTest("test_failed_result").run()
