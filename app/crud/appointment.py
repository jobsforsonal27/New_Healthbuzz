from sqlalchemy.orm import Session
from app.models.appointment import Appointment

def get_appointment_by_id(db:Session, patient_id:str):
    return db.query(Appointment).filter(Appointment.patient_id == patient_id).first()


def create_appointment(db:Session, data):
    appointment_data = data.dict()
    # Ensure we don't pass unexpected fields
    appointment_data.pop('id', None)
    appointment = Appointment(**appointment_data)
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

def modify_appointment(db:Session, appointment_id:str, data):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appointment:
        return None
    if appointment:
        print("got the appointment")
    for key, value in data.dict().items():
        setattr(appointment, key, value)
    db.commit()
    db.refresh(appointment)
    return appointment