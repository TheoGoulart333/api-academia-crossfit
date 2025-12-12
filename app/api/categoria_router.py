from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import SessionLocal
from app.models.categoria import Categoria
from app.schemas.categoria import CategoriaBase, CategoriaResponse

router = APIRouter(prefix="/categorias", tags=["Categorias"])

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/", response_model=CategoriaResponse)
async def criar_categoria(dados: CategoriaBase, db: AsyncSession = Depends(get_db)):
    categoria = Categoria(nome=dados.nome)
    db.add(categoria)
    await db.commit()
    await db.refresh(categoria)
    return categoria

@router.get("/", response_model=list[CategoriaResponse])
async def listar_categorias(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Categoria))
    return result.scalars().all()
