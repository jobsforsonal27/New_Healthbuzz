from pydantic import BaseModel
from datetime import date
class PatientCreate(BaseModel):
    user_id:str
    user_name:str
    dob:date
    gender:str
    address:str
class PatientResponse(BaseModel):
    id:str
    user_id:str
    user_name:str
    dob:date
    gender:str
    address:str

    model_config = {"from_attributes": True}