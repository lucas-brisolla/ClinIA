
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.agendamento_service import salvar_agendamento, listar_agendamentos

router = APIRouter()

class AgendamentoRequest(BaseModel):
    nome: str
    data: str
    horario: str
    servico: str

@router.post("/agendar")
async def agendar(req: AgendamentoRequest):
    agendamento = salvar_agendamento(req.dict())
    return {"status": "Agendamento salvo com sucesso", "data": agendamento}

@router.get("/agendamentos")
async def get_agendamentos():
    return listar_agendamentos()
