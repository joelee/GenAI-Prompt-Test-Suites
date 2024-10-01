from clients import import_client
from clients import OllamaClient


def test_load_client():
    client = import_client("ollama")
    assert client.__name__ == OllamaClient.__name__
