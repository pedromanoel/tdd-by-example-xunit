from testcase import TestCase

class WasRun(TestCase):

    def setup(self):
        self.log = "setup "

    def test_method(self):
        self.log = self.log + "test_method "
