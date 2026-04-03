from functools import lru_cache
import os

from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Jesh Chatbox Python"
    llm_mode: str = os.getenv("LLM_MODE", "mock")
    llm_api_url: str = os.getenv("LLM_API_URL", "https://api.example.com/v1/chat/completions")
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_model: str = os.getenv("LLM_MODEL", "gpt-compatible-model")
    system_prompt: str = os.getenv(
        "SYSTEM_PROMPT",
        "You are Jesh AI, a calm and practical assistant that answers clearly and briefly.",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

