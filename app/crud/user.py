from sqlalchemy.orm import Session
from app.models.users import User
from app.core.security import hash_pass,verify_pwd

def create_user(db:Session, email:str, password:str, role):
    user=User(
        email=email,
        hashed_pwd=hash_pass(password),
        role=role
    )
    db.add(user)
    db.commit()
    db.refresh(user)    
    return user
              
def authenticate_user(db:Session, email:str, password:str):
    user=db.query(User).filter(User.email==email).first()
    if not user:
        return None
    if not verify_pwd(password,user.hashed_pwd):
        return None
    return user 