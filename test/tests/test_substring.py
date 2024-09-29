from tests import import_test

run_test = import_test("substring")
RESPONSE = "To boldly go where no man has gone before."


def test_has_substring():
    assert run_test(RESPONSE, ["bold", "gone", "no man"])


def test_has_no_substring():
    assert not run_test(RESPONSE, ["dog", "woman"])


def test_case_insensitivity():
    assert run_test(RESPONSE, ["no MAN"])


def test_start_and_end_substring():
    assert run_test(RESPONSE, ["to", "fore."])
