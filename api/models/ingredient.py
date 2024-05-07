from typing import List
from pydantic import BaseModel

class Ingredient(BaseModel):
    id: int = None
    name: str 
    amount: float
    unit: str
    storage: str

class IngredientSearch(BaseModel):
    ingredients: List[str]
    num_results: int = 1