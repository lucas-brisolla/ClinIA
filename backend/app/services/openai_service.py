
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_resposta(mensagem_usuario):
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente virtual especializado em atendimento para clínicas estéticas."},
                {"role": "user", "content": mensagem_usuario}
            ]
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"
