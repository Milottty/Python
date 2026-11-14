from fastapi import FastAPI
from  database import read_movie, read_movies, create_movie, update_movie, delete_movie
app=FastAPI

@app.get("/")
def read_root():
    return {"message":"Hello World"}

