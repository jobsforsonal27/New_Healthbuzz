import uuid
from sqlalchemy import Column,String,Date
from app.core.database import BASE
class Patient(BASE):
    __tablename__ = "patients"
    id = Column(String,primary_key=True,default=lambda:str(uuid.uuid4()))
    user_id = Column(String,unique=True,index=True,nullable = False)
    user_name=Column(String,nullable=False)
    dob = Column(Date,nullable=False)
    gender = Column(String,nullable=False)
    address = Column(String,nullable=False)