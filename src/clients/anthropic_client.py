"""
Client for Anthropic API
"""
import os

from anthropic import Anthropic
from clients import BaseClient


ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")


class AnthropicClient(BaseClient):
    def __init__(self, config: dict):
        self.api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not set in environment variables")
        super().__init__(config)

    def request(self, prompt: str) -> str:
        client = Anthropic(api_key=self.api_key)

        message = client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=self.system_prompt,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content

    @property
    def system_prompt(self) -> str | None:
        return self.config.get("system_prompt", "You are an AI assistant.")
