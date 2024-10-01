"""
Client for OpenAI API
"""

import os

from openai import OpenAI

from clients import BaseClient


class OpenaiClient(BaseClient):
    def __init__(self, config: dict):
        self.api_key = os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set in environment variables")
        self.client = OpenAI(api_key=self.api_key)
        super().__init__(config)

    def request(self, prompt: str) -> str:
        kwargs = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
        }

        if self.model.startswith("gpt-") and not self.model.endswith("-instruct"):
            kwargs["messages"] = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ]
            response = self.client.chat.completions.create(**kwargs)
            return response.choices[0].message.content.strip()

        else:
            kwargs["prompt"] = self.prefix_system_prompt(prompt)
            response = self.client.completions.create(**kwargs)
            return response.choices[0].text.strip()

    @property
    def system_prompt(self) -> str | None:
        return self.config.get("system_prompt", "You are an AI assistant.")
