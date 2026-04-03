from fastapi import APIRouter, Depends

from app.config import Settings, get_settings
from app.models import ChatRequest, ChatResponse
from app.services.ai_client import AiClient


router = APIRouter(prefix="/api")


@router.get("/health")
async def health(settings: Settings = Depends(get_settings)) -> dict[str, str]:
    return {"status": "ok", "mode": settings.llm_mode}


@router.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest, settings: Settings = Depends(get_settings)) -> ChatResponse:
    client = AiClient(settings)
    result = await client.generate_reply(payload.message)
    return ChatResponse(reply=result.reply, provider=result.provider)

