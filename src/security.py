from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY", "10x5C.0_0T0N7")
if not isinstance(SECRET_KEY, str) or not SECRET_KEY.strip():
    raise ValueError("SECRET_KEY no está definido o es inválido. Configúralo en las variables de entorno.")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


hashed = hash_password("mi_contraseña")
print("Hash:", hashed)
print("Verificación:", verify_password("mi_contraseña", hashed))

token = create_access_token({"sub": "usuario123"})
print("Token:", token)
print("Token verificado:", verify_access_token(token))