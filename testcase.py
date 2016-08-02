class TestSuite:

    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestCase:

    def __init__(self, name):
        self.name = name

    def setup(self):
        pass

    def tear_down(self):
        pass

    def run(self, result):
        result.test_started()

        self.setup()
        try:
            getattr(self, self.name)()
        except:
            result.test_failed()

        self.tear_down()


class TestResult:

    def __init__(self):
        self.run_count = 0
        self.failure_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.failure_count += 1

    def summary(self):
        return "%d run, %d failed" % (self.run_count, self.failure_count)
