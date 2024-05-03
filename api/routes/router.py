from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends, Request

from models.ingredient import Ingredient
from models.user import User, UserLogin
from databases.database import SessionLocal

from middleware.middleware import authenticate, get_db

from services import ingredients
from services import users

router = APIRouter()

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
@authenticate
async def add_ingredient(request: Request, ingredient: Ingredient, db: Session = Depends(get_db)):
    return ingredients.add_ingredient(db, ingredient)
