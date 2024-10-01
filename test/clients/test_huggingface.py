from clients import import_client
from clients import HuggingfaceClient


def test_load_client():
    client = import_client("huggingface")
    assert client.__name__ == HuggingfaceClient.__name__
