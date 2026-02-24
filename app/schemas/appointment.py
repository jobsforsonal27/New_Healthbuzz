from pydantic import BaseModel
from datetime import date

class AppointmentCreate(BaseModel):
    doctor_name:str
    patient_id:str
    patient_name:str
    appointment_time:date
    status:str


class AppointmentResponse(BaseModel):
    id:str
    doctor_name:str
    patient_id:str
    patient_name:str
    appointment_time:date
    status:str

    class Config:
        orm_mode = True