"""
Client for Huggingface models
"""
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from clients import BaseClient


class HuggingfaceClient(BaseClient):
    def __init__(self, config: dict):
        self.auto_model = None
        self.auto_tokenizer = None
        super().__init__(config)

    def auto_init(self):
        """
        Initialize the model and tokenizer
        """
        if self.auto_tokenizer is None:
            self.auto_tokenizer = AutoTokenizer.from_pretrained(self.tokenizer)
        if self.auto_model is None:
            self.auto_model = AutoModelForCausalLM.from_pretrained(self.model)
            self.auto_model.to(self.device)
            self.auto_model.eval()

    def request(self, prompt: str) -> str:
        self.auto_init()

        # Encode the input prompt
        input_prompt = self.prefix_system_prompt(prompt)
        inputs = self.auto_tokenizer.encode(
            input_prompt, return_tensors=self.return_tensors
        ).to(self.device)

        # Generate the response
        with torch.no_grad():
            outputs = self.auto_model.generate(
                inputs,
                max_length=inputs.shape[1] + self.max_tokens,
                temperature=self.temperature,
                do_sample=self.temperature > 0.0,
                top_p=self.top_p,  # You can adjust these parameters
                top_k=self.top_k,
                eos_token_id=self.auto_tokenizer.eos_token_id,
                pad_token_id=self.auto_tokenizer.eos_token_id
            )

        # Decode the output
        output_text = self.auto_tokenizer.decode(
            outputs[0], skip_special_tokens=self.skip_special_tokens
        )

        # Remove the input prompt to get only the generated response
        return output_text.replace(input_prompt, "").strip()

    @property
    def max_length(self) -> int:
        return self.config.get("max_length", 50)

    @property
    def skip_special_tokens(self) -> bool:
        return self.config.get("skip_special_tokens", True)

    @property
    def return_tensors(self) -> str:
        return self.config.get("return_tensors", "pt")

    @property
    def tokenizer(self) -> str | None:
        return self.config.get("tokenizer", self.model)

    @property
    def device(self) -> str | None:
        return self.config.get("device", "cpu")
