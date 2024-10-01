from clients import import_client
from clients import OpenaiClient


def test_load_client():
    client = import_client("openai")
    assert client.__name__ == OpenaiClient.__name__
