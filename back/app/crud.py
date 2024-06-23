# back/crud.py
from sqlalchemy.orm import Session

from . import models
from . import schemas

def create_data(db: Session, data: schemas.DataCreate):
    db_data = models.Data(value=data.value)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_latest_data(db: Session):
    return db.query(models.Data).order_by(models.Data.id.desc()).first()

def get_all_data(db: Session):
    return db.query(models.Data).all()
