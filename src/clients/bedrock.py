import json

import boto3


def main(cfg, prompt):
    bedrock_runtime = boto3.client("bedrock-runtime")

    system_prompt = cfg.params.get("system_prompt")
    if system_prompt:
        prompt = f"{system_prompt}.\n{prompt}"

    # Prepare the request body
    request_body = {
        "prompt": prompt,
        "max_tokens": cfg.params.get("max_tokens", 100),
        "temperature": cfg.params.get("temperature", 0),
        "top_p": cfg.params.get("top_p", 0.95),
    }

    body = json.dumps(request_body)

    response = bedrock_runtime.invoke_model(
        modelId=cfg.model,
        contentType="application/json",
        accept="application/json",
        body=body,
    )

    # Parse and return the response
    response_body = json.loads(response["body"].read())
    return response_body["completion"]
