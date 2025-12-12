from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import SessionLocal
from app.models.centro import CentroTreinamento
from app.schemas.centro import CentroBase, CentroResponse

router = APIRouter(prefix="/centros", tags=["Centros"])

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/", response_model=CentroResponse)
async def criar_centro(dados: CentroBase, db: AsyncSession = Depends(get_db)):
    centro = CentroTreinamento(**dados.dict())
    db.add(centro)
    await db.commit()
    await db.refresh(centro)
    return centro

@router.get("/", response_model=list[CentroResponse])
async def listar_centros(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CentroTreinamento))
    return result.scalars().all()
