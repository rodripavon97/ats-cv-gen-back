from pydantic_settings import BaseSettings

class AuthConfig(BaseSettings):
    SECRET_KEY: str = "10x5C.0_0T0N7"  # Cambiar esto en producción!
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "postgresql://share_it_ats_user:10x5C.0_0T0N7@35.226.215.172:5432/share_it_ats"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


auth_config = AuthConfig()

