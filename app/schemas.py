from datetime import date   
from pydantic import BaseModel
from sqlalchemy import orm



class Record(BaseModel):
    id:int
    date:date
    country: str
    cases:int
    deaths: int
    recoveries:int
    
    
    class Config:
        orm_mode = True