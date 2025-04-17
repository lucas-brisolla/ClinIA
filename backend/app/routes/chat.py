
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.openai_service import gerar_resposta

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(req: ChatRequest):
    resposta = gerar_resposta(req.message)
    return {"response": resposta}
