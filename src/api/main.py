from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="EnvHealth API")

class PredictRequest(BaseModel):
    temp: float
    humidity: float
    pm25_lag_1: float
    pm25_lag_2: float
    pm25_lag_3: float

# Load model once at startup
model = joblib.load("models/pm25_model.joblib")

@app.get("/")
def read_root():
    return {"message": "Welcome to EnvHealth API! Use POST /predict to get PM2.5 predictions."}

@app.post("/predict")
def predict(req: PredictRequest):
    df = pd.DataFrame([req.dict()])
    pred = model.predict(df)[0]
    return {"predicted_pm25": float(pred)}
