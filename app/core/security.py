from jose import jwt
from datetime import datetime, timedelta,timezone

from passlib.context import CryptContext
from app.core.config import JWT_SECRET_KEY,JWT_ALGORITHM,ACCESS_TOKEN_EXPIRY_TIME


pwd_pattern=CryptContext(schemes=["bcrypt"])  

def hash_pass(password:str)->str:
    return pwd_pattern.hash(password)

def verify_pwd(password:str, hashed:str)->bool:
    return pwd_pattern.verify(password,hashed)

def create_access_token(data:dict):
    to_encode = data.copy()
    expiry = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRY_TIME)
    to_encode.update({"exp":expiry})
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
  

    
