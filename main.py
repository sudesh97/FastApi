import uvicorn
    # main.py
# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from typing import List

# from .database import get_db
# from .models import User
# from .schemas import UserSchema
from fastapi import FastAPI, Path
# from pymongo import MongoClient
# client=MongoClient()
app = FastAPI()

# client.admin.command("ping") 

print("Connected successfully")
# @app.get("/users/", response_model=List[UserSchema])
# def read_users(db: Session = Depends(get_db)):
#     users = db.query(User).all()
#     return users
@app.get("/hello1/{name}")
async def hello1(name:str=Path(...,min_length=3,
max_length=10)):
   return {"name": name}

@app.get("/hello/{name}")
async def hello(name):
   return {"name": name}

@app.get("/")
async def index():
   return {"message": "Hello World"}

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)