"""
Client for Ollama API
"""

import os

import requests
import yaml

from clients import BaseClient


class OllamaClient(BaseClient):
    def __init__(self, config: dict):
        self.api_url = os.environ.get("OLLAMA_API_URL")
        if not self.api_url:
            raise ValueError("OLLAMA_API_URL not set in environment variables")
        super().__init__(config)

    def request(self, prompt: str) -> str:
        payload = {"model": self.model, "prompt": prompt}
        response = requests.post(self.api_url, json=payload, stream=True)
        response.raise_for_status()
        response_text = ""
        for line in response.iter_lines():
            if line:
                data = line.decode("utf-8")
                response_json = yaml.safe_load(data)
                content = response_json.get("response", "")
                response_text += content
        return response_text.strip()
