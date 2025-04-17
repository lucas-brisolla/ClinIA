
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chat, agendamento

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api")
app.include_router(agendamento.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "ClinIA API ativa"}
