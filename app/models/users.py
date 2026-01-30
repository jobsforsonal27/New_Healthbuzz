import enum
import uuid

from sqlalchemy import Column, String, Boolean, Enum

from app.core.database import BASE

class UserRole(str,enum.Enum):
    patient="patient"
    doctor="doctor"
    pharmacy="pharmacy"
    insurance="insurance"
    admin="admin"

class User(BASE):
    __tablename__="users"
    
    id=Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email=Column(String, unique=True, index=True, nullable=False)
    hashed_pwd=Column(String, nullable=False)
    is_active=Column(Boolean, default=True)
    role=Column(Enum(UserRole), nullable=False)   



