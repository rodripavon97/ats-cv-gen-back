from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.logger_config import logger

DATABASE_URL = "postgresql://share_it_ats_user:10x5C.0_0T0N7@35.226.215.172:5432/share_it_ats"

engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        logger.critical(f"Error en la sesión de BD: {e}")
    finally:
        db.close()
