from clients import BedrockClient, import_client


def test_load_client():
    client = import_client("bedrock")
    assert client.__name__ == BedrockClient.__name__
