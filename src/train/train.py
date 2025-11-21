from ultralytics import YOLO
import argparse
import os

def main(args):
    model_size = args.model
    epochs = args.epochs
    imgsz = args.imgsz
    batch = args.batch
    data = os.path.join(os.path.dirname(__file__), '..', 'data.yaml')

    model = YOLO(model_size)
    model.train(data=data, epochs=epochs, imgsz=imgsz, batch=batch, name='rps_experiment')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="yolov8n.pt")
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--batch", type=int, default=16)
    args = parser.parse_args()
    main(args)
