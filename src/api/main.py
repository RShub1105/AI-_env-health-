from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI(title="EnvHealth API")

# -----------------------------
# Request model
# -----------------------------
class PredictRequest(BaseModel):
    temp: float
    humidity: float
    pm25_lag_1: float
    pm25_lag_2: float
    pm25_lag_3: float

# -----------------------------
# Load ML model (cloud-safe path)
# -----------------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../../models/pm25_model.joblib')
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

# -----------------------------
# Root endpoint
# -----------------------------
@app.get("/")
def read_root():
    return {"message": "Welcome to EnvHealth API! Use POST /predict to get PM2.5 predictions."}

# -----------------------------
# Prediction endpoint
# -----------------------------
@app.post("/predict")
def predict(req: PredictRequest):
    df = pd.DataFrame([req.dict()])
    pred = model.predict(df)[0]
    return {"predicted_pm25": float(pred)}

# -----------------------------
# For local testing only
# -----------------------------
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Cloud port fallback
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
