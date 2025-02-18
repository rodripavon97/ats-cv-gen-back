from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import CvCreate


router = APIRouter()

@router.post("/register/")
def create_cv(cv: CvCreate, db: Session = Depends(get_db)):
   
    return {"message": "User created successfully"}

