from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Contagem(BaseModel):
    contador: int


@app.get("/api/status")
def status():
    return {"status": "servidor online"}


@app.post("/api/contagem")
def receber_contagem(data: Contagem):
    print(f"Contagem recebida: {data.contador}")
    return {"status": "ok", "recebido": data.contador}


@app.put("/api/config")
def atualizar_config(cfg: dict):
    print("Config recebida:", cfg)
    return {"status": "config atualizada"}


@app.delete("/api/reset")
def resetar():
    print("reset solicitado pelo ESP")
    return {"status": "reset executado"}
