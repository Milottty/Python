import requests
from script import User
from typing import Dict
api_url="http://127.0.0.1:8000/user"

user_data:Dict[str,str| int]={"id":1,"name":"John","age":23,"email":"xyz@gmail.com", "gender":"Male"}
# user_data=User(id=1,name="John",age=21,email="xyz@gmail.com",gender="Male")
responses=requests.post(api_url,json=user_data)
print(responses.status_code)


