import os

from anthropic import Anthropic

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")


def main(cfg, prompt):
    if not ANTHROPIC_API_KEY:
        raise AttributeError("ANTHROPIC_API_KEY not set in environment variables")

    client = Anthropic(api_key=ANTHROPIC_API_KEY)

    message = client.messages.create(
        model=cfg.model,
        max_tokens=cfg.params.get("max_tokens", 100),
        temperature=cfg.params.get("temperature", 0),
        system=cfg.params.get("system_prompt", "You are an AI assistant."),
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content
