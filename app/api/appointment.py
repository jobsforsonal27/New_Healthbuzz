from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.appointment import AppointmentCreate,AppointmentResponse
from app.models.appointment import Appointment
from app.crud.appointment import create_appointment as crud_create_appointment, get_appointment_by_id, modify_appointment as crud_modify_appointment


router = APIRouter(prefix="/appointment",tags=["appointments"])


@router.post("/create",response_model=AppointmentResponse)
def create_appointment(data:AppointmentCreate, db:Session=Depends(get_db)):

    # Check if a patient already has an appointment at the same time
    if get_appointment_by_id(db, data.patient_id):
        raise HTTPException(status_code=400, detail = "Appointment already exists for this patient")

    return crud_create_appointment(db, data)

@router.put("/modify/{appointment_id}",response_model=AppointmentResponse)
def modify_appointment(appointment_id:str, data:AppointmentCreate, db:Session=Depends(get_db)):
    appointment = crud_modify_appointment(db, appointment_id, data)
    if not appointment:
        raise HTTPException(status_code=404, detail = "Appointment not found")
    return appointment