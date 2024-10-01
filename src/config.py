from os import environ, path

import yaml
import json
from case import Case
from client import Client

GENAI_TEST_CONFIG_FILE = environ.get("GENAI_TEST_CONFIG_FILE")


class Config:
    def __init__(self):
        file_path = GENAI_TEST_CONFIG_FILE
        if file_path is None:
            file_path = path.join(
                self.get_base_dir(),
                "config.yaml"
            )
        self.file_path = file_path
        self._config = None

    @property
    def config(self):
        if self._config is None:
            ext = self.file_ext
            with open(self.file_path) as file:
                if ext == ".json":
                    self._config = json.load(file)
                elif ext == ".yaml":
                    self._config = yaml.safe_load(file)
                else:
                    raise ValueError("Unsupported file type: {ext}")
        return self._config

    @property
    def clients(self):
        for c in self.config["clients"]:
            yield self._load_client(c)

    @property
    def cases(self):
        for c in self.config["test_cases"]:
            yield Case(c)

    @property
    def file_ext(self) -> str:
        return path.splitext(self.file_path)[1].lower()

    def to_json(self):
        return json.dumps(self.config, indent=4)

    @staticmethod
    def get_base_dir():
        return path.realpath(
            path.join(
                path.dirname(path.realpath(__file__)),
                ".."
            )
        )

    def load_client(self, type, model):
        for client in self.clients:
            if client.type == type and client.model == model:
                return self._load_client(client)
        return None

    @staticmethod
    def _load_client(self, client):
        client_type = client["type"]
        model = client["model"]
        del client["type"]
        del client["model"]
        return Client(client_type, model, params=client)


if __name__ == "__main__":
    config = Config()
    print(f"Loading config from: {config.file_path}")
    print(config.to_json())
