import os

import requests
import yaml

OLLAMA_API_URL = os.environ.get("OLLAMA_API_URL")


def main(cfg, prompt):
    if not OLLAMA_API_URL:
        raise AttributeError("OLLAMA_API_URL not set in environment variables")

    payload = {"model": cfg.model, "prompt": prompt}
    response = requests.post(OLLAMA_API_URL, json=payload, stream=True)
    response.raise_for_status()
    response_text = ""
    for line in response.iter_lines():
        if line:
            data = line.decode("utf-8")
            response_json = yaml.safe_load(data)
            content = response_json.get("response", "")
            response_text += content
    return response_text.strip()
