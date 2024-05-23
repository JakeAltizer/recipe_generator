from typing import List, Optional
from pydantic import BaseModel, Json
from datetime import datetime

class Recipe(BaseModel):
    name: str
    prep_time_minutes: int = None
    cook_time_minutes: int = None
    num_servings: int = None
    ingredients: List[str]
    instructions: List[str]
    summary: str = None
    credits: List[str] = None
