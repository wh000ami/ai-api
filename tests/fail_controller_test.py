import pytest
from fastapi.testclient import TestClient

from app.controller import app

client = TestClient(app)


def test_unkown_url():
    response = client.get("/unkown_url")
    assert response.status_code == 404
