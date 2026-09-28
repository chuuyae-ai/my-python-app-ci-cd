from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/api/v1/user")
def get_user(email: str):
    return {"id": 1, "name": "Ivan Ivanov", "email": "i.i.ivanov@mail.com"}

@app.post("/api/v1/user")
def create_user(user: User):
    return 1

@app.delete("/api/v1/user")
def delete_user(email: str):
    return None
