from pydantic import BaseModel

class DoctorCreate(BaseModel):
    user_id:str
    name: str
    specialization: str
    yoe: int

class DoctorResponse(BaseModel):
    id:str
    user_id:str
    name: str
    specialization: str
    yoe: int

    class Config:
        orm_mode = True