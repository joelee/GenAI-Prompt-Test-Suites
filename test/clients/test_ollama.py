from clients import OllamaClient, import_client


def test_load_client():
    client = import_client("ollama")
    assert client.__name__ == OllamaClient.__name__
