from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from .import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
 
@app.get('/')
def index():
    return {'Hello World'}
