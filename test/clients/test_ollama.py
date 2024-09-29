import os

import pytest
from client import Client

# load_dotenv()
OLLAMA_API_URL = os.environ.get("OLLAMA_API_URL")


def test_request():
    client = Client("ollama", "llama2-uncensored")

    if not OLLAMA_API_URL:
        with pytest.raises(AttributeError):
            client.request("test prompt")
        pytest.skip("Skipping OLLAMA client test.")

    response = client.request("How are you?")
    assert response
