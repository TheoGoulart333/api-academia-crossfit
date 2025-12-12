from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Atleta(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    centro_id = Column(Integer, ForeignKey("centros.id"))
    categoria = relationship("Categoria")
    centro = relationship("CentroTreinamento")
