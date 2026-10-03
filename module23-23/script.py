from typing import Optional
from pydantic import BaseModel,conint,constr
from fastapi import FastAPI

app=FastAPI()
class User(BaseModel):
    id:int
    name:str
    age:conint(gt=0)
    email:constr(min_length=5)
    gender:Optional[str]=None

@app.post("/user")
async def create_user(user:User):
    return user

def main():
    user1:User=User(id=1,name="John",age=21,email="xyz@gmail.com",gender="Male")
    user10:User=User(id=4,name="John",age=21,email="xyz@gmail.com",gender="Male")
    user11:User=User(id=5,name="John",age=21,email="xyz@gmail.com",gender="Male")
    user5:User=User(id=6,name="John",age=21,email="xyz@gmail.com",gender="Male")

    print(user1.name)

if __name__=="__main__":
    main()

