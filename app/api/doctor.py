from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.doctor import DoctorCreate,DoctorResponse
from app.models.doctor import Doctor
from app.crud.doctor import create_doctor as crud_create_doctor, get_user_by_id


router = APIRouter(prefix="/doctors",tags=["doctors"])


@router.post("/create",response_model=DoctorResponse)
def create_doctor(data:DoctorCreate, db:Session=Depends(get_db)):
    print(data.user_id)
    if get_user_by_id(db, data.user_id):
        raise HTTPException(status_code=400, detail = "Doctor already exists")
    
    return crud_create_doctor(db, data.user_id, data)