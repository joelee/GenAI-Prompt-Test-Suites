# ruff: noqa: F401
from .anthropic_client import AnthropicClient
from .base_client import BaseClient, ClientResponse
from .bedrock_client import BedrockClient
from .huggingface_client import HuggingfaceClient
from .ollama_client import OllamaClient
from .openai_client import OpenaiClient


def import_client(name):
    class_name = f"{name.title()}Client"
    try:
        return globals()[class_name]
    except KeyError as e:
        raise ImportError(f"Cannot import {class_name}") from e
