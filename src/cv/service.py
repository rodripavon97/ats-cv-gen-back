from sqlalchemy.orm import Session
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from models import Cv, User
import uuid
import os

class CVService:
    def __init__(self, db: Session):
        self.db = db

    def generate_pdf(self, cv_id: uuid.UUID) -> str:
        cv = self.db.query(Cv).filter(Cv.id == cv_id).first()
        if not cv:
            raise ValueError("CV no encontrado")

        user = self.db.query(User).filter(User.id == cv.user_id).first()
        if not user:
            raise ValueError("Usuario no encontrado")

        # Generar el PDF
        filename = f"cv_{cv.id}.pdf"
        c = canvas.Canvas(filename, pagesize=letter)

        # Agregar contenido al PDF
        c.drawString(100, 750, f"CV de {user.first_name} {user.last_name}")
        c.drawString(100, 730, f"Teléfono: {cv.telephone}")
        c.drawString(100, 710, f"Rol: {cv.role}")
        c.drawString(100, 690, f"Resumen: {cv.summary}")

        # Experiencia
        c.drawString(100, 650, "Experiencia:")
        y = 630
        for exp in cv.experiences:
            c.drawString(120, y, f"{exp.role} en {exp.company} ({exp.start_date} - {exp.end_date})")
            c.drawString(140, y - 15, exp.description)
            y -= 30

        # Habilidades
        c.drawString(100, y - 20, "Habilidades:")
        y -= 40
        for skill in cv.skills:
            c.drawString(120, y, f"{skill.title} - Nivel: {skill.level}")
            y -= 20

        # Guardar el PDF
        c.save()
        return filename