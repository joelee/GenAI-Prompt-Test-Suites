from tests import import_test

run_test = import_test("word")
RESPONSE = "To boldly go where no man has gone before."


def test_has_word():
    assert run_test(RESPONSE, ["boldly", "gone", "no man"])


def test_has_no_substring():
    assert not run_test(RESPONSE, ["bold", "here"])


def test_has_no_word():
    assert not run_test(RESPONSE, ["dog", "woman"])


def test_case_insensitivity():
    assert run_test(RESPONSE, ["BOLDly"])


def test_start_and_end_substring():
    assert run_test(RESPONSE, ["to", "before"])
