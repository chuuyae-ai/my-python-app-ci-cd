from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

users = [
    {"id": 1, "name": "Ivan Ivanov", "email": "i.i.ivanov@mail.com"},
    {"id": 2, "name": "Petr Petrov", "email": "p.p.petrov@mail.com"}
]

@app.get("/api/v1/user")
def get_user(email: str):
    for u in users:
        if u["email"] == email:
            return u
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/api/v1/user", status_code=201)
def create_user(user: User):
    for u in users:
        if u["email"] == user.email:
            raise HTTPException(status_code=409, detail="User already exists")
    new_id = max(u["id"] for u in users) + 1
    users.append({"id": new_id, "name": user.name, "email": user.email})
    return new_id

@app.delete("/api/v1/user", status_code=204)
def delete_user(email: str):
    for i, u in enumerate(users):
        if u["email"] == email:
            users.pop(i)
            return
    raise HTTPException(status_code=404, detail="User not found")
