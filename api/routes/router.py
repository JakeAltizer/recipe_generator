from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends, Request, Response

from models.ingredient import Ingredient
from models.user import User, UserLogin
from databases.database import SessionLocal

from middleware.middleware import authenticate, get_db

from services import ingredients
from services import users

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello!"}

@router.post("/users/register/")
async def register(user: User, db: Session = Depends(get_db)):
    return users.create_account(user, db)

@router.post("/users/login/")
async def login(credentials: UserLogin, response: Response, db: Session = Depends(get_db)):
    return users.login(credentials, response, db)

@router.post("/ingredients/")
@authenticate
async def add_ingredient(request: Request, ingredient: Ingredient, db: Session = Depends(get_db)):
    return ingredients.add_ingredient(db, ingredient)
