from os import path

import yaml
from case import Case
from client import Client


class Config:
    def __init__(self, file_path=None):
        if file_path is None:
            file_path = path.join(
                path.dirname(path.realpath(__file__)), "..", "config.yaml"
            )

        with open(file_path) as file:
            self.config = yaml.safe_load(file)

    @property
    def clients(self):
        for client in self.config["clients"]:
            type = client["type"]
            model = client["model"]
            del client["type"]
            del client["model"]
            yield Client(type, model, params=client)

    @property
    def cases(self):
        for case in self.config["test_cases"]:
            yield Case(case)
