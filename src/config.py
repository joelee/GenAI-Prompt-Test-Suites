from os import path
import pytest
import requests
import yaml

from client import Client


class Case:
    def __init__(self, test_case):
        self.test_case = test_case

    @property
    def name(self):
        return self.test_case["name"]

    @property
    def prompt(self):
        return self.test_case["prompt"]

    @property
    def expected_substrings(self):
        return self.test_case.get("expected_substrings")

    @property
    def forbidden_substrings(self):
        return self.test_case.get("forbidden_substrings")


class Config:
    def __init__(self, file_path=None):
        if file_path is None:
            file_path = path.join(path.dirname(path.realpath(__file__)), "..", "config.yaml")

        with open(file_path, "r") as file:
            self.config = yaml.safe_load(file)

    @property
    def clients(self):
        for client in self.config["clients"]:
            type = client["type"]
            model = client["model"]
            del(client["type"])
            del(client["model"])
            yield Client(type, model, params=client)

    @property
    def cases(self):
        for case in self.config["test_cases"]:
            yield Case(case)
