from testcase import TestCase

class WasRun(TestCase):

    def __init__(self, name):
        self.wasSetUp = None
        TestCase.__init__(self, name)

    def setup(self):
        self.wasRun = None
        self.wasSetUp = 1

    def test_method(self):
        self.wasRun = 1
