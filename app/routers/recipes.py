from pydantic import BaseModel
from typing import List, Optional
from models.recipe import RecipeBase

class RecipeBase(BaseModel):
    name: str
    description: Optional[str] = None
    ingredients: str
    instructions: str
    cuisine:str
    difficulty: str
    category_id: (Optional[int])
