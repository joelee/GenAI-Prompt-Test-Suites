"""
Client for Amazon Bedrock Runtime
"""
import json

import boto3

from clients import BaseClient



class BedrockClient(BaseClient):
    def request(self, prompt: str) -> str:
        bedrock_runtime = boto3.client("bedrock-runtime")

        # Prepare the request body
        request_body = {
            "prompt": self.prefix_system_prompt(prompt),
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "top_p": self.top_p,
        }

        body = json.dumps(request_body)

        response = bedrock_runtime.invoke_model(
            modelId=self.model,
            contentType="application/json",
            accept="application/json",
            body=body,
        )

        # Parse and return the response
        response_body = json.loads(response["body"].read())
        return response_body["completion"]
