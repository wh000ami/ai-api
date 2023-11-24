import pytest
from fastapi.testclient import TestClient

from app.controller import app

client = TestClient(app)


def test_unkown_url():
    response = client.get("/unkown_url")
    assert response.status_code == 404


def test_wrong_model_name():
    response = client.post("/generate", json={"model": "wrong", "message": "hello friend"})
    assert response.status_code == 405
    assert response.json() == {'detail': {'error': 'Model name must be `gtp2` or `gtp2-large` not wrong'}}