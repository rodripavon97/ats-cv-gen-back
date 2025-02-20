from uuid import UUID
from pydantic import BaseModel, EmailStr, constr
from datetime import datetime, date
from typing import Optional, List


class SkillBase(BaseModel):
    title: constr(min_length=1, max_length=10)
    level: Optional[str] = None


class ExperienceBase(BaseModel):
    role: constr(min_length=1, max_length=30)
    company: constr(min_length=1, max_length=100)
    start_date: date
    end_date: Optional[date] = None
    description: Optional[str] = None


class SoftSkillBase(BaseModel):
    title: constr(min_length=1, max_length=15)


class CertificationBase(BaseModel):
    name: constr(min_length=1, max_length=65)
    institution: constr(min_length=1, max_length=65)
    date: date
    description: Optional[str] = None


class AcademicBase(BaseModel):
    title: constr(min_length=1, max_length=65)
    institution: constr(min_length=1, max_length=65)
    start_date: date
    end_date: Optional[date] = None
    description: Optional[str] = None


class ProjectBase(BaseModel):
    title: constr(min_length=1, max_length=65)
    tech: Optional[str] = None
    description: Optional[str] = None


class ProfileBase(BaseModel):
    name: constr(min_length=1, max_length=20)
    url: Optional[str] = None


class LanguageBase(BaseModel):
    speech: constr(min_length=1, max_length=30)
    level: Optional[str] = None
    certificate: Optional[constr(min_length=1, max_length=30)] = None


class CvCreate(BaseModel):
    telephone: Optional[int] = None
    role: constr(min_length=1, max_length=30)
    summary: Optional[str] = None
    user_id: UUID  

    skills: List[SkillBase] = []
    experiences: List[ExperienceBase] = []
    soft_skills: List[SoftSkillBase] = []
    certifications: List[CertificationBase] = []
    academics: List[AcademicBase] = []
    projects: List[ProjectBase] = []
    profiles: List[ProfileBase] = []
    languages: List[LanguageBase] = []

    class Config:
        from_attributes = True
