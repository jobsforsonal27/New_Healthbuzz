from sqlalchemy.orm import Session
from app.models.patients import Patient

def get_user_by_id(db:Session,user_id:str):
    return db.query(Patient).filter(Patient.user_id == user_id).first()
print("function calling")
def create_patient(db:Session,user_id:str,data):
    print("inside create patient crud")
    patient = Patient(**data.dict())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient