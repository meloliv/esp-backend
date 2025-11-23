from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from .database import Base

class Contagem(Base):
    __tablename__ = "contagens"

    id = Column(Integer, primary_key=True, index=True)
    contador = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())
