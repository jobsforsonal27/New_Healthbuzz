from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.core.database import engine, BASE

BASE.metadata.create_all(bind=engine)

app= FastAPI(title="Auth Services")
app.include_router(auth_router)






