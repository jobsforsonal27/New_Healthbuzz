import uuid
from sqlalchemy import Column, String, Date, Integer
from app.core.database import BASE

class Appointment(BASE):
    __tablename__ = "appointments"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    doctor_name = Column(String,nullable=False)
    patient_id = Column(String,nullable=False)
    patient_name = Column(String, nullable=False)
    appointment_time = Column(Date, nullable=False)
    status = Column(String,nullable=False, default= "Booked")  # e.g., scheduled, completed, canceled