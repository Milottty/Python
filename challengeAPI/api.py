
from fastapi import  FastAPI

app = FastAPI()
@app.get("/")

def root():
    return{
    "book1":{
       "title":"Uvjesi",
        "author":"Miloti",
        "year": 2026,
        "genre":"SDI"

    },
    "book2":{
       "title":"Lul kuqet mbi mur",
        "author":"Uvjesi",
        "year": 1999,
        "genre":"SDI"

    },
    "book3":{
       "title":"Shkolla Digjitale",
        "author":"Une",
        "year": 2000,
        "genre":"SDI"

    },
}
