from datetime import datetime
from fastapi import Request

from sqlalchemy.orm import Session
from models.ingredient import Ingredient
from databases.db_ingredient import DBIngredient
from middleware.middleware import get_current_user


def add_ingredient(ingredient: Ingredient, request: Request, db: Session):
    current_user = get_current_user(request)

    db_ingredient = DBIngredient(user_id=current_user.id, name=ingredient.name, amount=ingredient.amount,
                                    unit=ingredient.unit, storage=ingredient.storage, created_at=datetime.now())
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return {"message": "Ingredient added!"}