import argparse
import cv2
from ..app.model import RPSModel
from ..app.utils import decide_winner

def main(args):
    model = RPSModel()
    img_a = cv2.imread(args.img_a)
    img_b = cv2.imread(args.img_b)

    a = model.predict_single(img_a)
    b = model.predict_single(img_b)
    res = decide_winner(a, b)
    print(res)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--img_a", required=True)
    parser.add_argument("--img_b", required=True)
    args = parser.parse_args()
    main(args)
