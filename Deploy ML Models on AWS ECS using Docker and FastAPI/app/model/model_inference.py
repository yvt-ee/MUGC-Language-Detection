# Importing packages
import re
import pickle
from pathlib import Path

import warnings
warnings.simplefilter("ignore")


BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/svm_model.pickle", "rb") as f:
    model = pickle.load(f)


classes = [
    "0",
    "1"
]


def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    pred = model.predict([text])
    return classes[pred[0]]



if __name__ == '__main__':
    text = 'Ciao, come stai?'
    detect = predict_pipeline(text)
    print('Prediction :', detect)