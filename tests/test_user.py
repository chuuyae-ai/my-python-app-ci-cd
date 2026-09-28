from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

users = [
    {"id": 1, "name": "Ivan Ivanov", "email": "i.i.ivanov@mail.com"},
    {"id": 2, "name": "Petr Petrov", "email": "p.p.petrov@mail.com"}
]

def test_get_existed_user():
    response = client.get("/api/v1/user", params={"email": users[0]["email"]})
    assert response.status_code == 200
    assert response.json() == users[0]

def test_get_unexisted_user():
    response = client.get("/api/v1/user", params={"email": "nonexistent@mail.com"})
    assert response.status_code == 404

def test_create_user_valid():
    response = client.post("/api/v1/user", json={
        "name": "New User",
        "email": "new.user@mail.com"
    })
    assert response.status_code == 201
    assert isinstance(response.json(), int)

def test_create_user_duplicate():
    response = client.post("/api/v1/user", json={
        "name": "Duplicate User",
        "email": users[0]["email"]
    })
    assert response.status_code == 409

def test_delete_user():
    response = client.delete("/api/v1/user", params={"email": users[1]["email"]})
    assert response.status_code == 204
