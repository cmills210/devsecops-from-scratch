from fastapi.testclient import TestClient
from app.main import app
from app.main import add

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "DevSecOps From Scratch API"}

def test_health():
    response = client.get("/health")
    assert response.json() == {"status": "ok"}

def test_add():
    assert add(2, 3) == 5