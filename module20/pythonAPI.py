# JSON DATA

# {
#   "name": "Uvejsi",
#   "age": "18",
#   "address": {
#     "Country": "Kosova",
#     "City": "Prishtina",
#     "Zip Code": "10000",
#     "Street": "BREGIII"
#   },
#   "contacts": [
#     {
#       "type": "email",
#       "value": "uviuvi123@gmail.com"
#     },
#     {
#       "type": "phone",
#       "value": "+38344123456"
#     },
#     {
#       "type": "Linkedin",
#       "value": "Uvejsi"
#     }
#   ]
# }
#

from fastapi import  FastAPI

app = FastAPI()
@app.get("/")

def root():
    return  {
  "name": "Uvejsi",
  "age": "18",
  "address": {
    "Country": "Kosova",
    "City": "Prishtina",
    "Zip Code": "10000",
    "Street": "BREGIII"
  },
  "contacts": [
    {
      "type": "email",
      "value": "uviuvi123@gmail.com"
    },
    {
      "type": "phone",
      "value": "+38344123456"
    },
    {
      "type": "Linkedin",
      "value": "Uvejsi"
    }
  ]
}