from typing import List
from datetime import datetime

from sqlalchemy.orm import Session
from fastapi import HTTPException

from databases.db_recipe import DBRecipe
from models.recipe import Recipe
from services.ingredients import process_ingredients

def process_instructions(instructions_list: List):
    processed_instructions = []
    for step, instruction in enumerate(instructions_list, start=1):
        processed_instructions.append({"step":step, "instruction":instruction})
    return processed_instructions

def add_new_recipe(recipe: Recipe, db: Session):
    total_time_minutes = recipe.prep_time_minutes + recipe.cook_time_minutes
    
    # process recipe ingredients
    ingredients_dict = process_ingredients(recipe.ingredients)

    # process recipe instructions
    instructions_dict = process_instructions(recipe.instructions)

    # check if name and credits exist already
    existing_recipe = db.query(DBRecipe).filter(
        DBRecipe.name == recipe.name,
        DBRecipe.credits == recipe.credits).first()

    if existing_recipe:
        raise HTTPException(status_code=404, 
                            detail="Recipe: " + recipe.name + "by: " + str(recipe.credits) + " already exists.")

    # Add recipe to the database
    created_at = datetime.now()
    updated_at = created_at
    db_recipe = DBRecipe(name=recipe.name, prep_time_minutes=recipe.prep_time_minutes,
                         cook_time_minutes=recipe.cook_time_minutes, total_time_minutes=total_time_minutes,
                         num_servings=recipe.num_servings, ingredients=ingredients_dict,
                         instructions=instructions_dict, summary=recipe.summary,
                         credits=recipe.credits, created_at=created_at, updated_at=updated_at)

    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    return {"message": "Recipe added!"}