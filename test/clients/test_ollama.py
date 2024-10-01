from clients import OllamaClient, import_client


def test_load_client():
    client = import_client("ollama")
    assert client.__name__ == OllamaClient.__name__


if __name__ == "__main__":
    # Pre-requisite: `ollama run llama2
    client = import_client("ollama")
    con = client({"model": "llama2", "type": "ollama"})
    print(con.request("Hello. Please introduce yourself."))
