from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os

class Mistral_c:
    def __init__(self, api_key, model="mistral-large-latest"):
        self.api_key = api_key
        self.model = model
        self.client = MistralClient(api_key=self.api_key)

    def prompt(self, user_input):
        message = ChatMessage(role="user", content=user_input)
        chat_response = self.client.chat(model=self.model, messages=[message])
        return chat_response.choices[0].message.content

    def print_prompt(self, prompt):
        print(prompt)