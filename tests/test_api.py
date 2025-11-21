from fastapi.testclient import TestClient
from src.app.main import app
import os

client = TestClient(app)

def test_dummy():
    assert True
