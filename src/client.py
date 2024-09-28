import os
import pytest
from anthropic import Anthropic
import openai
import requests
import boto3
import json


class Client:
    def __init__(self, type, model, params=None):
        self.type = type
        self.model = model
        self.params = params if params else {}

    def request(self, prompt):
        return getattr(self, self.type)(prompt)

    @property
    def disabled(self):
        return self.params.get("disabled", False)

    def ollama(self, prompt):
        ollama_url = os.environ.get("OLLAMA_API_URL")
        if not ollama_url:
            pytest.skip("OLLAMA_API_URL not set in environment variables")
        payload = {
            "model": self.model,
            "prompt": prompt
        }
        try:
            response = requests.post(ollama_url, json=payload, stream=True)
            response.raise_for_status()
            response_text = ''
            for line in response.iter_lines():
                if line:
                    data = line.decode('utf-8')
                    response_json = yaml.safe_load(data)
                    content = response_json.get('response', '')
                    response_text += content
            return response_text.strip()
        except requests.exceptions.RequestException as e:
            pytest.fail(f"API request failed: {e}")
        except Exception as e:
            pytest.fail(f"An error occurred: {e}")

    def openai(self, prompt):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            pytest.skip("OPENAI_API_KEY not set in environment variables")
        kwargs = {
            "engine": self.model,
            "max_tokens": self.params.get("max_tokens", 100),
            "temperature": self.params.get("temperature", 0.0)
        }
        if self.params.get("prompt_only", False):
            system_prompt = self.params.get("system_prompt")
            if system_prompt:
                prompt = f"{system_prompt}.\n{prompt}"
            kwargs["prompt"] = prompt
        else:
            system_prompt = self.params.get("system_prompt", "You are an AI assistant.")
            kwargs["messages"] = [
                { "role": "system", "content": system_prompt },
                { "role": "user", "content": prompt },
            ] 
        
        response = openai.Completion.create(**kwargs)
        return response.choices[0].text.strip()

    def anthropic(self, prompt):
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            pytest.skip("ANTHROPIC_API_KEY not set in environment variables")

        client = Anthropic(api_key=api_key)

        message = client.messages.create(
            model=self.model,
            max_tokens=self.params.get("max_tokens", 100),
            temperature=self.params.get("temperature", 0),
            system=self.params.get("system_prompt", "You are an AI assistant."),
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content
        
    def bedrock(self, prompt):
        bedrock_runtime = boto3.client('bedrock-runtime')

        system_prompt = self.params.get("system_prompt")
        if system_prompt:
            prompt = f"{system_prompt}.\n{prompt}"

        # Prepare the request body
        request_body = {
            "prompt": prompt,
            "max_tokens": self.params.get("max_tokens", 100),
            "temperature": self.params.get("temperature", 0),
            "top_p": self.params.get("top_p", 0.95),
        }

        body = json.dumps(request_body)

        response = bedrock_runtime.invoke_model(
            modelId=self.model,
            contentType="application/json",
            accept="application/json",
            body=body
        )

        # Parse and return the response
        response_body = json.loads(response['body'].read())
        return response_body['completion']
