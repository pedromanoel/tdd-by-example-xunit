class TestCase:

    def __init__(self, name):
        self.name = name

    def setup(self):
        pass

    def tear_down(self):
        pass

    def run(self):
        result = Result()
        result.test_started()

        self.setup()
        getattr(self, self.name)()
        self.tear_down()

        return result

class Result:

    def __init__(self):
        self.run_count = 0

    def test_started(self):
        self.run_count += 1

    def summary(self):
        return "%d run, 0 failed" % self.run_count
