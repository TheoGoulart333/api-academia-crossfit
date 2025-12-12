from pydantic import BaseModel

class AtletaBase(BaseModel):
    nome: str
    idade: int
    categoria_id: int
    centro_id: int

class AtletaResponse(AtletaBase):
    id: int
    class Config:
        orm_mode = True
