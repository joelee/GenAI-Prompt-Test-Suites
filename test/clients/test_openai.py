from clients import OpenaiClient, import_client


def test_load_client():
    client = import_client("openai")
    assert client.__name__ == OpenaiClient.__name__
