# Rock Paper Scissors YOLOv8 API.
# Rock Paper Scissors API con YOLOv8

## 📄 Descripción

Este proyecto contiene una **API en FastAPI** para predecir resultados de **Rock-Paper-Scissors** usando un modelo entrenado con **YOLOv8**.
Incluye:

* Código fuente de la API (`src/app/main.py`)
* Dockerfile para ejecutar la API en contenedor
* Scripts de entrenamiento (`yolov8/train.py`)
* Enlace recomendado para descargar los pesos entrenados (`yolov8/best.pt`). Dada la dimensión se envian por correo electronico
* README reproducible y guía de uso

---

## 🛠 Requisitos

* Python 3.10
* [YOLOv8](https://docs.ultralytics.com/)
* FastAPI
* Uvicorn
* Docker (opcional)

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecutar API localmente

```bash
uvicorn src.app.main:app --reload
```

* API disponible en: `http://localhost:8000`
* Documentación automática: `http://localhost:8000/docs`

**Ejemplo de request con `curl`:**

```bash
curl -X POST "http://localhost:8000/predict" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@test_image.jpg;type=image/jpeg"
```

Respuesta ejemplo:

```json
{
  "predictions": [
    {"label": "rock", "confidence": 0.95}
  ]
}
```

---

## 🐳 Ejecutar API con Docker

1. Construir la imagen Docker:

```bash
docker build -t rps-api .
```

2. Ejecutar el contenedor:

```bash
docker run -d -p 8000:8000 rps-api
```

* API accesible en `http://localhost:8000`

---

## 🏋️ Entrenamiento YOLOv8

Script de entrenamiento: `yolov8/train.py`

```bash
# Instalar ultralytics si no está
pip install ultralytics

# Entrenar el modelo
python yolov8/train.py --data yolov8/dataset --epochs 100 --img-size 640

# Guardar pesos en yolov8/best.pt
```



## 📦 Pesos del modelo


```markdown
Descargar pesos YOLOv8: [enlace de descarga]
```

* Los usuarios deberán descargar y colocar `best.pt` en `yolov8/best.pt`.

---

## 🗂 Estructura del proyecto

```
rock-paper-scissors-eval/
├─ src/app/main.py           # API FastAPI
├─ yolov8/train.py           # Script de entrenamiento
├─ yolov8/dataset/           # Dataset (opcional)
├─ yolov8/best.pt            # Pesos entrenados (enlace externo)
├─ requirements.txt          # Dependencias
├─ Dockerfile                # Contenedor API
├─ README.md                 # Esta guía
└─ .gitignore                # Archivos a ignorar
```

---

## 🔗 Notas importantes

* Docker Desktop debe estar instalado para usar contenedor.
* La API responde con:

```json
{"status":"API working"}
```

* Asegúrate de instalar todas las dependencias antes de entrenar o ejecutar.
* Los pesos grandes deben descargarse externamente para mantener el repositorio ligero y reproducible.

