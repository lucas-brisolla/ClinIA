
from datetime import datetime

agendamentos_mock = []

def salvar_agendamento(data):
    agendamento = {
        "nome": data["nome"],
        "data": data["data"],
        "horario": data["horario"],
        "servico": data["servico"],
        "criado_em": datetime.now().isoformat()
    }
    agendamentos_mock.append(agendamento)
    return agendamento

def listar_agendamentos():
    return agendamentos_mock
