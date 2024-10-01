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
        for test in tests:
            yield TestDef(test)

    @property
    def forbidden(self):
        tests = self.test_case.get("forbidden", [])
        for test in tests:
            yield TestDef(test)


class TestDef:
    def __init__(self, definition):
        self._def = definition
        self.run_test = import_test(self.type)

    @property
    def type(self):
        return self._def["type"]

    @property
    def definition(self):
        return self._def

    def validate(self, response):
        return self.run_test(self._def).validate(response)
