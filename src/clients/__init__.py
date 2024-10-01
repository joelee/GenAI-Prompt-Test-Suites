# ruff: noqa: F401
from .anthropic_client import AnthropicClient
from .base_client import BaseClient, ClientResponse
from .bedrock_client import BedrockClient
from .huggingface_client import HuggingfaceClient
from .ollama_client import OllamaClient
from .openai_client import OpenaiClient


def import_client(name):
    """
    Import a client by name.
    """
    class_name = f"{name.title()}Client"
    try:
        return globals()[class_name]
    except KeyError as e:
        raise ImportError(f"Cannot import {class_name}") from e


def quick_test(params):
    """
    Quick test to check if the client is working.
    Usage:
    ```
    from clients import quick_test
    quick_test({
        "model": "gpt-4o-mini",
        "type": "openai",
        "max_tokens": 100,
        "temperature": 0.0,
        "system_prompt": "You are Spock from Vulcan, an AI assistant.",
        "prompt": "Hello. Please introduce yourself. Are you human?"
    })
    ```
    """
    client = import_client(params["type"])
    prompt = params["prompt"]
    del params["prompt"]
    con = client(params)
    print(con.request(prompt))
