from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Request, Response

from models.ingredient import Ingredient, IngredientSearch
from models.user import User, UserLogin
from models.recipe import Recipe

from middleware.middleware import authenticate, get_db

from services import users, ingredients, recipes

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
    return ingredients.add_ingredient(ingredient, request, db)

@router.post("/recipes/add/")
@authenticate
async def add_recipe(request: Request, recipe: Recipe, db: Session = Depends(get_db)):
    return recipes.add_new_recipe(recipe, db)
