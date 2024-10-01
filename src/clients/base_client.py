"""
Abstract base class for all AI clients.
"""
from abc import ABC, abstractmethod
import time


class ClientResponse:
    def __init__(self, response: str, elapsed_time: float | None = None):
        self._response = response
        self._elapsed_time = elapsed_time

    @property
    def response(self) -> str:
        return self._response

    @property
    def elapsed_time(self) -> float:
        return self._elapsed_time


class BaseClient(ABC):
    def __init__(self, config: dict):
        self.config = config
        if not config.get("type"):
            raise ValueError("Client type is required")
        if not config.get("model"):
            raise ValueError("Client model is required")

    @abstractmethod
    def request(self, prompt: str) -> str:
        pass

    @property
    def type(self) -> str:
        return self.config.get("type")

    @property
    def model(self) -> str:
        return self.config.get("model")

    @property
    def disabled(self) -> bool:
        return self.config.get("disabled", False)

    @property
    def max_tokens(self) -> int:
        return self.config.get("max_tokens", 100)

    @property
    def temperature(self) -> float:
        return self.config.get("temperature", 0.0)

    @property
    def top_p(self) -> float:
        return self.config.get("top_p", 0.95)

    @property
    def top_k(self) -> float:
        return self.config.get("top_k", 50)

    @property
    def system_prompt(self) -> str | None:
        return self.config.get("system_prompt")

    @property
    def device(self) -> str | None:
        return self.config.get("device")

    @property
    def tokenizer(self) -> str | None:
        return self.config.get("tokenizer")

    @property
    def prompt_only(self) -> bool:
        return self.config.get("prompt_only", False)

    def prefix_system_prompt(self, prompt: str) -> str:
        system_prompt = self.system_prompt
        if system_prompt:
            return f"{system_prompt}\n\n{prompt}"
        return prompt

    def profile_request(self, prompt: str) -> str:
        start_time = time.time()
        response = self.request(prompt)
        elapsed_time = time.time() - start_time
        return ClientResponse(response, elapsed_time)
