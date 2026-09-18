from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_task():
    response = client.post("/tasks", json={"title": "Review project with agent"})

    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Review project with agent"
    assert data["completed"] is False
    assert "id" in data


def test_list_tasks():
    client.post("/tasks", json={"title": "Run tests"})

    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)