from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.auth.router import router as auth_router
from src.database import init_db
from cv.router import router as cv_router

DATABASE_URL = "postgresql://share_it_ats_user:10x5C.0_0T0N7@35.226.215.172:5432/share_it_ats"

def lifespan(app: FastAPI):
    print("Iniciando la aplicación...")
    init_db()  
    yield
    print("Apagando la aplicación...")

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
app.include_router(cv_router, prefix="/cv", tags=["CV"])

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API de CV Generator!"}

print(f"DATABASE_URL: {DATABASE_URL}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
