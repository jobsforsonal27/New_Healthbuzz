from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import DATABASE_URL

engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autoflush=False, bind=engine)

BASE=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    except Exception as msg:
        print(f"Database error: {msg}")
        raise
    finally:
        db.close()




    