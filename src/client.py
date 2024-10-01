from clients import ClientResponse, import_client


class Client:
    def __init__(self, config: dict):
        self.config = config
        if config.get("type") is None:
            raise ValueError("Client type is required")
        if config.get("model") is None:
            raise ValueError("Client model is required")
        self.client = import_client(self.type)(config)

    def request(self, prompt: str) -> str:
        return self.client.request(prompt)

    def profile_request(self, prompt: str) -> ClientResponse:
        return self.client.profile_request(prompt)

    @property
    def type(self) -> str:
        return self.config.get("type")

    @property
    def model(self) -> str:
        return self.config.get("model")

    @property
    def disabled(self) -> bool:
        return self.params.get("disabled", False)
