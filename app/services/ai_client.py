from __future__ import annotations

from dataclasses import dataclass

import httpx

from app.config import Settings


@dataclass
class AiResult:
    reply: str
    provider: str


class AiClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def generate_reply(self, user_message: str) -> AiResult:
        if self.settings.llm_mode.lower() == "mock":
            return self._mock_reply(user_message)
        return await self._remote_reply(user_message)

    def _mock_reply(self, user_message: str) -> AiResult:
        normalized = user_message.strip().lower()

        if "project" in normalized:
            reply = (
                "A strong next step is to break your idea into features, data flow, "
                "and one working milestone you can ship first."
            )
        elif "python" in normalized:
            reply = (
                "Python is a great fit for fast AI prototypes because the ecosystem "
                "makes APIs, web apps, and data handling simple."
            )
        else:
            reply = (
                "I heard you say: "
                f"'{user_message.strip()}'. "
                "In mock mode I can still help brainstorm, summarize, and shape ideas."
            )

        return AiResult(reply=reply, provider="mock")

    async def _remote_reply(self, user_message: str) -> AiResult:
        headers = {
            "Authorization": f"Bearer {self.settings.llm_api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.settings.llm_model,
            "messages": [
                {"role": "system", "content": self.settings.system_prompt},
                {"role": "user", "content": user_message},
            ],
            "temperature": 0.7,
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(self.settings.llm_api_url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

        reply = self._extract_reply(data)
        return AiResult(reply=reply, provider="remote")

    def _extract_reply(self, data: dict) -> str:
        choices = data.get("choices", [])
        if choices:
            message = choices[0].get("message", {})
            content = message.get("content")
            if isinstance(content, str) and content.strip():
                return content.strip()

        if "output_text" in data and isinstance(data["output_text"], str):
            return data["output_text"].strip()

        return "The AI provider responded, but no readable text was returned."

