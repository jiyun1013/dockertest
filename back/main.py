from typing import List  # 추가해야 할 부분

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from back import crud, models, schemas
from back.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/add/", response_model=schemas.Data)
def add_data(data: schemas.DataCreate, db: Session = Depends(get_db)):
    return crud.create_data(db=db, data=data)

@app.get("/get/", response_model=schemas.Data)
def get_data(db: Session = Depends(get_db)):
    db_data = crud.get_latest_data(db)
    if db_data is None:
        raise HTTPException(status_code=404, detail="No data found")
    return db_data

@app.get("/get_all/", response_model=List[schemas.Data])  # List 임포트 추가
def get_all_data(db: Session = Depends(get_db)):
    return crud.get_all_data(db)
