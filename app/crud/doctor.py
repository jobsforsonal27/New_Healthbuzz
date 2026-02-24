from sqlalchemy.orm import Session
from app.models.doctor import Doctor

def get_user_by_id(db:Session,user_id:str):
    return db.query(Doctor).filter(Doctor.user_id == user_id).first()

def create_doctor(db:Session,user_id:str,data):
    doctor_data = data.dict()
    doctor_data.pop('user_id', None)
    doctor = Doctor(user_id=user_id, **doctor_data)
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor