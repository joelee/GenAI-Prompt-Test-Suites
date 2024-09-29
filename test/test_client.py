from client import Client


def test_client():
    client = Client("ollama", "llama2")
    assert client.type == "ollama"
    assert client.model == "llama2"
    assert not client.disabled


# TODO: Mock calls
