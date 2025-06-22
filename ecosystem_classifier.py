import streamlit as st
import joblib
import numpy as np

# Load trained model (ensure file is in same directory or provide full path)
model = joblib.load('E:\EDUNET GREEN AI\ecosystem.pkl')

# Label mapping (reverse of training)
label_mapping = {0: "healthy", 1: "at risk", 2: "degraded"}

# Streamlit app UI
st.title("🌿 Ecosystem Health Classifier")

st.write("Provide environmental parameters below:")

# Input fields
wq = st.number_input("💧 Water Quality:", min_value=0.0, max_value=100.0, value=50.0)
aqi = st.number_input("🌫 Air Quality Index (AQI):", min_value=0.0, max_value=500.0, value=100.0)
bdi = st.number_input("🦋 Biodiversity Index (BDI):", min_value=0.0, max_value=1.0, value=0.5)
vc = st.number_input("🌳 Vegetation Cover (%):", min_value=0.0, max_value=100.0, value=60.0)
sph = st.number_input("🌱 Soil pH:", min_value=0.0, max_value=14.0, value=7.0)

# Prediction
if st.button("🔍 Predict Ecosystem Health"):
    input_data = np.array([[wq, aqi, bdi, vc, sph]])
    prediction = model.predict(input_data)[0]
    predicted_label = label_mapping[prediction]

    st.success(f"🌍 Predicted Ecosystem Health: **{predicted_label.upper()}**")
