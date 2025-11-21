from fastapi import FastAPI, UploadFile, File
from src.app.model import yolo_model
from src.app.utils import predict_image

app = FastAPI(title="Rock-Paper-Scissors API")

@app.get("/")
def home():
    return {"status": "API working"}

@app.post("/predict")
async def predict(player_a: UploadFile = File(...), player_b: UploadFile = File(...)):
    result_a = await predict_image(yolo_model, player_a)
    result_b = await predict_image(yolo_model, player_b)

    # ganador
    classes = ["Paper", "Rock", "Scissors"]

    rules = {
        ("Rock", "Scissors"): "Rock vence a Scissors",
        ("Scissors", "Paper"): "Scissors vence a Paper",
        ("Paper", "Rock"): "Paper vence a Rock"
    }

    winner = "tie"
    reason = "Same gesture"

    if result_a["prediction"] == "undecided" or result_b["prediction"] == "undecided":
        winner = "undecided"
        reason = "Low confidence"
    else:
        key = (result_a["prediction"], result_b["prediction"])
        if key in rules:
            winner = "player_a"
            reason = rules[key]
        elif (key[1], key[0]) in rules:
            winner = "player_b"
            reason = rules[(key[1], key[0])]

    return {
        "player_a": result_a,
        "player_b": result_b,
        "winner": winner,
        "reason": reason
    }
