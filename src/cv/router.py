from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from database import get_db
from .service import CVService
import uuid

router = APIRouter()

@router.get("/generate-pdf/{cv_id}")
async def generate_cv_pdf(cv_id: uuid.UUID, db: Session = Depends(get_db)):
    cv_service = CVService(db)
    try:
        # Generar el PDF usando el servicio
        pdf_filename = cv_service.generate_pdf(cv_id)
        # Devolver el archivo PDF como respuesta
        return FileResponse(pdf_filename, media_type="application/pdf", filename=pdf_filename)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))