from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session


from app.core.database import get_db
from app.schemas.patient import PatientCreate,PatientResponse
from app.models.patients import Patient
from app.crud.patient import get_user_by_id

router = APIRouter(prefix="/patients",tags=["patients"])


@router.post("/create",response_model=PatientResponse)
def create_patient(data:PatientCreate, db:Session=Depends(get_db)):
    print(data.user_id)
    if get_user_by_id(db, data.user_id):
        raise HTTPException(status_code=400, detail = "Patient already exists")
    from app.crud.patient import create_patient as create_patient_crud
    return create_patient_crud(db,data.user_id,data)


