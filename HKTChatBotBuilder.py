from decouple import config
from langchain.llms.base import LLM
from typing import List, Optional
import requests
import json
from pydantic import Field, Extra

class HKTChatBotBuilder(LLM):
    max_token: int = 10000
    model_name: str = Field("gpt-4", alias="model")
    temperature: float = 0
    top_p: float = 0.9
    max_retries: int = 6
    history = []
    bot_builder_api_base: str = config('BOT_BUILDER_API_BASE')
    bot_builder_api_key: str = config('BOT_BUILDER_API_KEY')
    bot_builder_group_chat: str = config('BOT_BUILDER_GROUP_CHAT')

    def __init__(self):
        super().__init__()

    @property
    def _llm_type(self) -> str:
        return "BotBuilder"

    def _call(self, content: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.bot_builder_api_key
        }

        data = json.dumps({
            "approach": "rrr",
            "history": [
                {
                    "role": "user",
                    "content": content
                }
            ],
            "overrides": {
                "model": self.model_name
            }
        })

        response = requests.post(self.bot_builder_api_base + self.bot_builder_group_chat, headers=headers, data=data)
        resp = response.json()
        return resp['answer']
