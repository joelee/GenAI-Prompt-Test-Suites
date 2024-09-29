import os

import openai

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


def main(cfg, prompt):
    if not OPENAI_API_KEY:
        raise AttributeError("OPENAI_API_KEY not set in environment variables")

    kwargs = {
        "engine": cfg.model,
        "max_tokens": cfg.params.get("max_tokens", 100),
        "temperature": cfg.params.get("temperature", 0.0),
    }
    if cfg.params.get("prompt_only", False):
        system_prompt = cfg.params.get("system_prompt")
        if system_prompt:
            prompt = f"{system_prompt}.\n{prompt}"
        kwargs["prompt"] = prompt
    else:
        system_prompt = cfg.params.get("system_prompt", "You are an AI assistant.")
        kwargs["messages"] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]

    response = openai.Completion.create(**kwargs)
    return response.choices[0].text.strip()
