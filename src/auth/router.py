import logging
from fastapi import APIRouter

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logging.info("Cargando rutas de autenticación...")

@router.get("/")
def read_auth_root():
    return {"message": "Endpoint de autenticación funcionando"}

@router.post("/login")
def login_user():
    return {"message": "Usuario autenticado"}
