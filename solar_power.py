import streamlit as st
import joblib as jb
import numpy as np

# Load trained model
model = jb.load(r"E:\EDUNET GREEN AI\solar_power_prediction_model.pkl")

st.title("🔆 Solar Power Output Predictor")

st.write("Provide the environmental conditions below to predict the solar power output:")

# Inputs
temp = st.number_input("🌡 Temperature (°C):", min_value=-10.0, max_value=50.0, value=25.0)
humidity = st.number_input("💧 Humidity (%):", min_value=0.0, max_value=100.0, value=50.0)
irradiance = st.number_input("☀ Solar Irradiance (W/m²):", min_value=0.0, max_value=1500.0, value=500.0)
wind_speed = st.number_input("🍃 Wind Speed (m/s):", min_value=0.0, max_value=30.0, value=5.0)

# Prediction
if st.button("🔍 Predict Solar Power Output"):
    new_input = np.array([[temp, humidity, irradiance, wind_speed]])
    prediction = model.predict(new_input)
    st.success(f"⚡ Predicted Solar Power Output: {prediction[0]:,.2f} watts")
    st.caption("Thank you for using the predictor! ☀")