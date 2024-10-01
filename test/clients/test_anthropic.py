from clients import AnthropicClient, import_client


def test_load_client():
    client = import_client("anthropic")
    assert client.__name__ == AnthropicClient.__name__
