from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
from models import Contagem

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ContagemPayload(BaseModel):
    contador: int


@app.post("/api/contagem")
def receber_contagem(data: ContagemPayload, db: Session = Depends(get_db)):
    registro = Contagem(contador=data.contador)
    db.add(registro)
    db.commit()
    db.refresh(registro)

    return {
        "status": "salvo",
        "id": registro.id,
        "contador": registro.contador,
        "hora": str(registro.created_at),
    }

@app.get("/api/contagens")
def listar_contagens(db: Session = Depends(get_db)):
    dados = db.query(Contagem).order_by(Contagem.id.desc()).all()
    return dados
