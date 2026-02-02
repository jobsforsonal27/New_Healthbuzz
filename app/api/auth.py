from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.crud import user

from app.schemas.user import ResetPasswordSchema, UserCreate,Token,UserLogin,ResetPasswordSchema
from app.crud.user import create_user,authenticate_user,reset_password

from app.core.database import get_db
from app.core.security import create_access_token

router=APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/create_user")
def register(user:UserCreate,db:Session=Depends(get_db)):
    return create_user(db,user.email,user.password,user.role)

@router.post("/login",response_model=Token)
def login(user:UserLogin,db:Session=Depends(get_db)):
    db_user=authenticate_user(db,user.email,user.password)
    if not db_user:
        raise HTTPException(status_code=401,detail="Invalid Credentials")
    access_token=create_access_token(data={"sub":db_user.email})
    return {"access_token":access_token,"token_type":"bearer"}

@router.put("/reset_password")
def Password(data: ResetPasswordSchema,db: Session = Depends(get_db)):
    print("calling reset password  ")
    db_user=reset_password(db,data.email,data.new_password)
    return db_user







