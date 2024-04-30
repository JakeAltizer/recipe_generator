from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

from models.ingredient import Ingredient
from models.user import User, UserLogin
from databases.database import SessionLocal

from services import ingredients
from services import users

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

@router.post("/users/register/")
async def register(user: User, db: Session = Depends(get_db)):
    return users.create_account(user, db)

@router.post("/users/login/")
async def login(credentials: UserLogin, db: Session = Depends(get_db)):
    return users.login(credentials, db)

@router.post("/ingredients/")
async def add_ingredient(ingredient: Ingredient, db: Session = Depends(get_db)):
    return ingredients.add_ingredient(db, ingredient)
