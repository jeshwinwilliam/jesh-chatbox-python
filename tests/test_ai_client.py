from app.config import Settings
from app.services.ai_client import AiClient


def test_mock_reply_mentions_mock_provider() -> None:
    client = AiClient(Settings(llm_mode="mock"))
    result = client._mock_reply("Help me with a Python project")

    assert result.provider == "mock"
    assert result.reply

