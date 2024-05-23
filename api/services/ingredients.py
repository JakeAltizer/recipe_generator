from datetime import datetime
from fastapi import Request

from typing import List

from sqlalchemy.orm import Session
from models.ingredient import Ingredient
from databases.db_ingredient import DBIngredient
from middleware.middleware import get_current_user


def process_ingredients(ingredients_list: List[str]):
    # TODO: use llm to determine ingredient and base ingredient
    catigorized_ingredients = []
    for ingredient in ingredients_list:
        base_ingredient = ""
        catigorized_ingredients.append({"ingredient": ingredient,
                                      "base_ingredient": base_ingredient})

    # TODO: Get id of each ingredient
    # get id of each ingredient in db
    # if no result add to database (add_ingredient())
    processed_ingredients = []
    for ingredient in ingredients_list:
        ingredient_id = 0
        processed_ingredients.append({"ingredient": ingredient,
                                      "ingredient_id": ingredient_id})

    return processed_ingredients


def add_ingredient(ingredient: Ingredient, request: Request, db: Session):
    current_user = get_current_user(request)

    db_ingredient = DBIngredient(user_id=current_user.id, name=ingredient.name, amount=ingredient.amount,
                                    unit=ingredient.unit, storage=ingredient.storage, created_at=datetime.now())
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return {"message": "Ingredient added!"}
