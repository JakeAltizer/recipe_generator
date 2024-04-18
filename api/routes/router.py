from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

from models.ingredient import Ingredient
from databases.database import SessionLocal

from services import ingredients

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def root():
    return {"message": "Hello! Add ingredients here!"}

@router.post("/ingredients/")
async def add_ingredient(ingredient: Ingredient, db: Session = Depends(get_db)):
    return ingredients.add_ingredient(db, ingredient)
