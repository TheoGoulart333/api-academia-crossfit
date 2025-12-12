from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import SessionLocal
from app.models.atleta import Atleta
from app.schemas.atleta import AtletaBase, AtletaResponse

router = APIRouter(prefix="/atletas", tags=["Atletas"])

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/", response_model=AtletaResponse)
async def criar_atleta(dados: AtletaBase, db: AsyncSession = Depends(get_db)):
    atleta = Atleta(**dados.dict())
    db.add(atleta)
    await db.commit()
    await db.refresh(atleta)
    return atleta

@router.get("/", response_model=list[AtletaResponse])
async def listar_atletas(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Atleta))
    return result.scalars().all()
