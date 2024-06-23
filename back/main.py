# back/main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from back import crud, models, schemas
from back.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 여기에 허용할 클라이언트의 주소를 추가
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
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
