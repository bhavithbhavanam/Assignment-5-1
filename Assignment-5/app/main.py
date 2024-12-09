from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, get_db
# Create database tables
Base.metadata.create_all(bind=engine)
# Set off the FastAPI app
app = FastAPI()
# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Sandwich Maker API"}

# Create a sandwich
@app.post("/sandwiches/", response_model=schemas.Sandwich)
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return crud.create_sandwich(db=db, sandwich=sandwich)

# Read all sandwiches
@app.get("/sandwiches/", response_model=list[schemas.Sandwich])
def read_sandwiches(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_sandwiches(db, skip=skip, limit=limit)

# Read a single sandwich
@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich)
def read_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    db_sandwich = crud.get_sandwich(db, sandwich_id=sandwich_id)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return db_sandwich

# Update a sandwich
@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich)
def update_sandwich(sandwich_id: int, sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    db_sandwich = crud.update_sandwich(db, sandwich_id, sandwich)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return db_sandwich

# Delete a sandwich
@app.delete("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich)
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    db_sandwich = crud.delete_sandwich(db, sandwich_id)
    if db_sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return db_sandwich
