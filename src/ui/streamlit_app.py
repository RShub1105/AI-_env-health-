import streamlit as st
import requests

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="EnvHealth — PM2.5 Predictor",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------- STYLES ----------
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #e0f7fa 0%, #f1f8e9 100%);
            color: #222;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 2.2rem;
            color: #00796b;
            margin-bottom: 1rem;
        }
        .footer {
            text-align: center;
            margin-top: 2rem;
            color: #555;
            font-size: 0.9rem;
        }
        .stButton>button {
            background-color: #00796b;
            color: white;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            font-size: 1rem;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #004d40;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<div class='title'>🌍 EnvHealth — PM2.5 Air Quality Predictor</div>", unsafe_allow_html=True)
st.write("Estimate **PM2.5 concentration** based on temperature, humidity, and past readings.")

# ---------- INPUTS ----------
col1, col2 = st.columns(2)

with col1:
    temp = st.number_input("🌡️ Temperature (°C)", min_value=-10.0, max_value=60.0, value=25.0)
    humidity = st.number_input("💧 Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
    pm25_lag_1 = st.number_input("PM2.5 (1-day lag)", min_value=0.0, value=35.0)

with col2:
    pm25_lag_2 = st.number_input("PM2.5 (2-day lag)", min_value=0.0, value=33.0)
    pm25_lag_3 = st.number_input("PM2.5 (3-day lag)", min_value=0.0, value=30.0)

# ---------- PREDICTION ----------
st.markdown("---")

if st.button("🚀 Predict Air Quality"):
    payload = {
        "temp": temp,
        "humidity": humidity,
        "pm25_lag_1": pm25_lag_1,
        "pm25_lag_2": pm25_lag_2,
        "pm25_lag_3": pm25_lag_3,
    }

    with st.spinner("Predicting air quality..."):
        try:
            API_URL = "http://127.0.0.1:8000/predict"
            resp = requests.post(API_URL, json=payload, timeout=5)

            if resp.status_code == 200:
                result = resp.json()["predicted_pm25"]
                st.success(f"✅ Predicted PM2.5: **{result:.2f} µg/m³**")

                if result < 30:
                    st.info("🌿 Air quality is **Good** — minimal health risk.")
                elif result < 60:
                    st.warning("😐 Air quality is **Moderate** — sensitive groups may be affected.")
                else:
                    st.error("⚠️ Air quality is **Poor** — take precautions!")

            else:
                st.error(f"Server error: {resp.status_code}")
        except Exception as e:
            st.error(f"Failed to connect to API. Error: {e}")

# ---------- FOOTER ----------
st.markdown("<div class='footer'>Made with ❤️ using FastAPI + Streamlit</div>", unsafe_allow_html=True)
