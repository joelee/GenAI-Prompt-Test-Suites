import pytest
from client import Client


def test_client():
    client = Client("ollama", "llama2")
    assert client.type == "ollama"
    assert client.name == "llama2"

# TODO: Mock calls
