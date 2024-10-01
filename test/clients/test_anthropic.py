from clients import import_client
from clients import AnthropicClient


def test_load_client():
    client = import_client("anthropic")
    assert client.__name__ == AnthropicClient.__name__
