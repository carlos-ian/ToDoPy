from fastapi import FastAPI
from database import engine, Base
import models 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

from auth_routes import auth_router

app.include_router(auth_router)