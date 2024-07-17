# tests/test_user.py
from fastapi.testclient import TestClient
from app.user import app

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert response.json() == {"msg": "User registered successfully"}

def test_register_user_already_exists():
    client.post("/register", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    })
    response = client.post("/register", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Username already registered"}
