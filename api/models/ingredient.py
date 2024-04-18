from pydantic import BaseModel

class Ingredient(BaseModel):
    id: int = None
    name: str 
    amount: int
    unit: str
    storage: str