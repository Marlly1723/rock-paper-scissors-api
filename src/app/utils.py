import io
from PIL import Image

CONFIDENCE_THRESHOLD = 0.4

async def predict_image(model, upload_file):
    image_bytes = await upload_file.read()
    img = Image.open(io.BytesIO(image_bytes))

    results = model.predict(img)

    best_pred = None

    for r in results:
        for b in r.boxes:
            conf = float(b.conf[0])
            cls = int(b.cls[0])
            if best_pred is None or conf > best_pred["confidence"]:
                best_pred = {
                    "prediction": model.names[cls],
                    "confidence": conf,
                    "bbox": b.xyxy[0].tolist()
                }

    if best_pred is None or best_pred["confidence"] < CONFIDENCE_THRESHOLD:
        return {"prediction": "undecided", "confidence": 0.0, "bbox": []}

    return best_pred
