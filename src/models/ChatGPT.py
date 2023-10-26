import os
import openai
from models.AbstractLanguageModel import AbstractLanguageModel


class ChatGPT(AbstractLanguageModel):
    def __init__(self) -> None:
        super().__init__("ChatGPT")

    def ask(self, prompt: str, reask: bool) -> str:
        if not reask:
            prompt = self._INTRODUCTION_TO_QUESTION + prompt
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self._INTRODUCTION_TO_QUESTION + prompt}
            ]
        )
        return completion.choices[0].message.content

    def _load_model(self) -> None:
        openai.api_key = os.getenv("OPENAI_API_KEY")
