import bcrypt
from jose import JWTError, jwt
from .models import Token
from datetime import datetime, timezone, timedelta
import time

SECRET_KEY = 'bluebird'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE = 30

def verify_password(plain_password: str, hashed_password: str):
    print("verifying password")
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def get_password_hash(password: str):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
