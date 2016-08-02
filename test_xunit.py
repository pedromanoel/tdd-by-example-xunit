from wasrun import WasRun
from testcase import TestCase

class TestCaseTest(TestCase):
    """Test if the TestCase is working"""

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert(test.log == "setup test_method ")

TestCaseTest("test_template_method").run()
