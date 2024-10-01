from clients import import_client
from clients import BedrockClient


def test_load_client():
    client = import_client("bedrock")
    assert client.__name__ == BedrockClient.__name__
