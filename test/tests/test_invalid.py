import pytest
from tests import import_test


def test_invalid_test_case():
    with pytest.raises(FileNotFoundError):
        import_test("invalid_test_case")
