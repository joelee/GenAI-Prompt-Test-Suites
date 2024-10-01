from clients import HuggingfaceClient, import_client


def test_load_client():
    client = import_client("huggingface")
    assert client.__name__ == HuggingfaceClient.__name__
