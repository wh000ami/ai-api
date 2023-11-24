import pytest
from fastapi.testclient import TestClient

from app.controller import app

client = TestClient(app)


def test_healths_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "health"}


def test_generate_model_url():
    response = client.post("/generate", json={"model": "gpt2", "message": "hello friend"})
    assert response.status_code == 200
    assert response.json().get("answer")
