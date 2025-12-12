from fastapi import FastAPI
from app.api.categoria_router import router as categoria_router
from app.api.centro_router import router as centro_router
from app.api.atleta_router import router as atleta_router

app = FastAPI(title="API de Academia Crossfit")

app.include_router(categoria_router)
app.include_router(centro_router)
app.include_router(atleta_router)

@app.get("/")
async def home():
    return {"message": "API funcionando!"}
