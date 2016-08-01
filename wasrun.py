from testcase import TestCase

class WasRun(TestCase):

    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def test_method(self):
        self.wasRun = 1
