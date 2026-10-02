from typing import Any, Dict, List


class LLMService:
    def __init__(self, api_key: str | None = None, model: str = "gpt-4o-mini"):
        self.api_key = api_key
        self.model = model

    def generate(self, prompt: str, **kwargs: Any) -> str:
        return f"Generated response for prompt: {prompt[:120]}..."

    def embed(self, text: str) -> List[float]:
        return [0.1, 0.2, 0.3]
