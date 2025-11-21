import requests

# URL de la API
url = "http://127.0.0.1:8000/predict"

# Imagen de prueba
file_path = "test_image.jpg"

# Abrir el archivo y enviar POST
with open(file_path, "rb") as f:
    files = {"file": (file_path, f, "image/jpeg")}
    response = requests.post(url, files=files)

# Mostrar resultado
print("Status code:", response.status_code)
print("Response JSON:", response.json())
from fastapi.testclient import TestClient
from src.app.main import app
import os

client = TestClient(app)

def test_dummy():
    assert True
