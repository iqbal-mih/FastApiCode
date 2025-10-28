from fastapi import FastAPI
from App.schemas import HeartFeatures, PredictionResponse
import joblib
import numpy as np
from pathlib import Path

app = FastAPI()

# load the trained model file (joblib) -- adjust relative path if needed
MODEL_PATH = Path(__file__).resolve().parents[1] / "model" / "heart_disease_model.joblib"
if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
model = joblib.load(str(MODEL_PATH))

FEATURES = [
    "age","sex","cp","trestbps","chol","fbs","restecg",
    "thalach","exang","oldpeak","slope","ca","thal",
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {"model_type": "RandomForestClassifier", "features": FEATURES}

@app.post("/predict", response_model=PredictionResponse)
def predict(data: HeartFeatures):
    arr = np.array([[data.age, data.sex, data.cp, data.trestbps, data.chol,
                     data.fbs, data.restecg, data.thalach, data.exang, data.oldpeak,
                     data.slope, data.ca, data.thal]])
    pred = int(model.predict(arr)[0])
    prob = float(model.predict_proba(arr).max())
    return PredictionResponse(prediction=pred, probability=prob)