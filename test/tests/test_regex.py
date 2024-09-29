from tests import import_test

run_test = import_test("regex")
RESPONSE = "To boldly go where no man has gone before."


def test_has_match():
    assert run_test(RESPONSE, ["bold", "has gone", "no.man"])


def test_has_no_substring():
    assert not run_test(RESPONSE, ["dog", "woman"])


def test_start_and_end_substring():
    assert run_test(RESPONSE, ["^[Tt]o", "fore.$"])
