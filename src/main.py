from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn

from src.auth.router import router as auth_router
from src.logger_config import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("✅ Iniciando la aplicación")
    yield
    logger.info("❌ Apagando la aplicación")

app = FastAPI(
    title="CV Generator API",
    description="API para la generación de CVs y autenticación.",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API de CV Generator!"}


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True, log_config=None)