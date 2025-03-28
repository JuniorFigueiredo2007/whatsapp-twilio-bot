print(">>> Iniciando aplicação FastAPI")

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/webhook")
async def receber_mensagem(request: Request):
    form = await request.form()
    from_number = form.get("From") or form.get("from")
    body = form.get("Body") or form.get("body")

    print(f"Mensagem recebida de {from_number}: {body}")
    return PlainTextResponse("Recebido com sucesso!")

@app.get("/")
def home():
    return {"status": "online"}
