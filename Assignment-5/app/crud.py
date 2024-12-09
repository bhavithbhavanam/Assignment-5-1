from sqlalchemy.orm import Session
from . import models, schemas
def get_sandwiches(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Sandwich).offset(skip).limit(limit).all()

def get_sandwich(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def create_sandwich(db: Session, sandwich: schemas.SandwichCreate):
    db_sandwich = models.Sandwich(name=sandwich.name, ingredients=sandwich.ingredients, price=sandwich.price)
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def update_sandwich(db: Session, sandwich_id: int, sandwich: schemas.SandwichCreate):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich:
        db_sandwich.name = sandwich.name
        db_sandwich.ingredients = sandwich.ingredients
        db_sandwich.price = sandwich.price
        db.commit()
        db.refresh(db_sandwich)
    return db_sandwich

def delete_sandwich(db: Session, sandwich_id: int):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich:
        db.delete(db_sandwich)
        db.commit()
    return db_sandwich
