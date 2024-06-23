# back/schemas.py
from pydantic import BaseModel

class DataBase(BaseModel):
    value: str

class DataCreate(DataBase):
    pass

class Data(DataBase):
    id: int

    class Config:
        orm_mode = True
