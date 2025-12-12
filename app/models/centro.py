from sqlalchemy import Column, Integer, String
from app.core.database import Base

class CentroTreinamento(Base):
    __tablename__ = "centros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
