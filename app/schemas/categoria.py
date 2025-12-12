from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nome: str

class CategoriaResponse(CategoriaBase):
    id: int
    class Config:
        orm_mode = True
