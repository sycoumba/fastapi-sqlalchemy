from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, responses
from .import models, schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from starlette.responses import RedirectResponse


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    )
#Dependency
def get_db():
    try:
        db = SessionLocal
        yield db
    finally:
     db.close()
    
 
@app.get('/')
def main():
    return RedirectResponse(url="/docs/")


@app.get("/records/", response_model =List[schemas.Record])
def show_records(db: Session = Depends(get_db)):
    records =db.query(models.Record).all()
    return records