# EnvHealth AI

Real-time PM2.5 Prediction & Air Quality Monitoring Dashboard using AI/ML, FastAPI, Streamlit, and Prometheus + Grafana.

---

## Project Architecture

![Architecture](https://raw.githubusercontent.com/RShub1105/AI-_env-health-/main/Architech%20of%20the%20project.png)

---

## Dashboard Screenshot

![Dashboard](https://raw.githubusercontent.com/RShub1105/AI-_env-health-/main/screenshot%20pm%202.5%20env%20helath.png)

---

## Features

- Predicts next-hour PM2.5 levels using Random Forest
- Real-time API with FastAPI
- Interactive Streamlit dashboard
- Prometheus + Grafana monitoring for metrics
- Beginner-friendly, fully containerized with Docker

---

## Tech Stack

- Python 3.10+, FastAPI, Streamlit  
- Pandas, NumPy, scikit-learn  
- Prometheus, Grafana  
- Docker & Docker Compose  

---


---
✅ **Key Notes for Images:**  
- Use the `raw.githubusercontent.com` URL, not the `blob` link.  
- That’s why your previous images didn’t show.  

I can also **make it even shorter and “GitHub sidebar-ready”** if you want it **ultra-minimal for recruiters / job-ready portfolio**.  

Do you want me to do that version too?


## Quick Start

1. Clone the repo  
```bash
git clone https://github.com/RShub1105/AI-_env-health-.git
cd AI-_env-health-

pip install -r requirements.txt

uvicorn src.api.main:app --reload --port 8000
streamlit run src/ui/streamlit_app.py
