from config import Config


def test_config_clients():
    cfg = Config()
    for client in cfg.clients:
        assert client.model
        assert client.type


def test_config_cases():
    cfg = Config()
    for client in cfg.cases:
        assert client.name
        assert client.prompt
        assert client.expected
