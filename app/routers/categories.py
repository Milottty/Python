from fastapi import FastAPI
from category import CategoryBase
import database

router = FastAPI(
    prefix="/categories",
    tags=["categories"]
)

@router.post("/")
def create_category(category: CategoryBase):
    try:
        category_id = database.create_category(category)
        return {"message": "Category created successfully", "category_id": category_id}
    except Exception as e:
        return {"message": "Error creating category", "error": str(e)}

@router.get("/")
def get_categories():
   return database.get_categories()

@router.get("/{category_id}")
def get_category(category_id: int):
    category = database.get_category(category_id)
    if category:
        return category
    else:
        return {"message": "Category not found"}