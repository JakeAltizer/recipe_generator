from datetime import datetime
from sqlalchemy.orm import Session
from models.ingredient import Ingredient
from databases.db_ingredient import DBIngredient


def add_ingredient(db: Session, ingredient: Ingredient):
    db_ingredient = DBIngredient(name=ingredient.name, amount=ingredient.amount,
                                    unit=ingredient.unit, storage=ingredient.storage, created_at=datetime.now())
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return {"message": "Ingredient added!"}