import uuid
from sqlalchemy import Column,String,Date,Integer
from app.core.database import BASE

class Doctor(BASE):
    __tablename__ = "doctors"

    id = Column(String,primary_key=True,default=lambda:str(uuid.uuid4()))
    user_id = Column(String,unique=True,index=True,nullable = False)
    name = Column(String,nullable=False)
    specialization = Column(String,nullable=False)
    yoe = Column(Integer,nullable=False)