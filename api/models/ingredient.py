from pydantic import BaseModel

class Ingredient(BaseModel):
    id: int = None
    name: str 
    amount: float
    unit: str
    storage: str