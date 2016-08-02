class TestCase:

    def __init__(self, name):
        self.name = name

    def setup(self):
        pass

    def tear_down(self):
        pass

    def run(self):
        self.setup()
        method = getattr(self, self.name)
        method()
        self.tear_down()
