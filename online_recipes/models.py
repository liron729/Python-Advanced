from pydantic import BaseModel

class RecipeCreate(BaseModel):
    title: str
    description: str
    ingredients: list[str]

class Recipe(RecipeCreate):
    id: int