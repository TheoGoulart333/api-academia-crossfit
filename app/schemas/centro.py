from pydantic import BaseModel

class CentroBase(BaseModel):
    nome: str
    endereco: str

class CentroResponse(CentroBase):
    id: int
    class Config:
        orm_mode = True
