from fastapi import FastAPI
from database import create_table
from routers import categories, recipes

app = FastAPI()


@app.on_event("startup")
def startup():
    create_table()


app.include_router(categories.router)
app.include_router(recipes.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Online Recipe Book"}