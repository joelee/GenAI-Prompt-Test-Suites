import pytest
from clients import import_client


def test_invalid_client():
    with pytest.raises(ImportError):
        import_client("invalid_client")
