import json
from os import environ, path

import yaml
from case import Case
from client import Client

GENAI_TEST_CONFIG_FILE = environ.get("GENAI_TEST_CONFIG_FILE")


class Config:
    def __init__(self):
        file_path = GENAI_TEST_CONFIG_FILE
        if file_path is None:
            file_path = path.join(self.get_base_dir(), "config.yaml")
        self.file_path = file_path
        self._config = None
        self._ext = None

    @property
    def config(self) -> dict:
        if self._config is None:
            with open(self.file_path) as file:
                if self.file_ext == ".json":
                    self._config = json.load(file)
                elif self.file_ext == ".yaml":
                    self._config = yaml.safe_load(file)
                else:
                    raise ValueError('Unsupported file type: "{self.file_ext}"')
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
        if self._ext is None:
            ext = path.splitext(self.file_path)[1] or ""
            self._ext = ext.lower()
        return self._ext

    def to_json(self):
        return json.dumps(self.config, indent=4)

    @staticmethod
    def get_base_dir():
        return path.realpath(path.join(path.dirname(path.realpath(__file__)), ".."))

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
