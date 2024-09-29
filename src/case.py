from tests import import_test


class Case:
    def __init__(self, test_case):
        self.test_case = test_case

    @property
    def name(self):
        return self.test_case["name"]

    @property
    def prompt(self):
        return self.test_case["prompt"]

    @property
    def expected(self):
        tests = self.test_case.get("expected", [])
        for name in tests:
            yield CaseTest(name, tests[name])

    @property
    def forbidden(self):
        tests = self.test_case.get("forbidden", [])
        for name in tests:
            yield CaseTest(name, tests[name])


class CaseTest:
    def __init__(self, name, values):
        self.name = name
        self.values = values
        self.run_test = import_test(name)

    def validate(self, response):
        return self.run_test(response, self.values)
