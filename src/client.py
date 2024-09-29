from clients import import_client


class Client:
    def __init__(self, type, model, params=None):
        self.type = type
        self.model = model
        self.params = params if params else {}

    def request(self, prompt):
        client = import_client(self.type)
        return client(self, prompt)

    @property
    def disabled(self):
        return self.params.get("disabled", False)
