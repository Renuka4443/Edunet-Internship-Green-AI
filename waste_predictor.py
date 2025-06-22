import streamlit as st
import joblib
import numpy as np

# Load model and scaler only
model = joblib.load('logistic_regression_model.pkl')
scaler = joblib.load('scaler.pkl')

# Manually define label mapping based on your model classes
label_mapping = {0: 'Organic', 1: 'Plastic', 2: 'Metal', 3: 'Glass'}  # Change this to your actual mapping

st.title("♻ Waste Type Classifier (Logistic Regression)")

# User Input Fields
weight = st.number_input("⚖ Weight (g):", min_value=0.0, max_value=3.0, value=0.0)
color = st.number_input("🎨 Color Intensity (numeric):", min_value=0.0, max_value=1.0, value=0.0)
texture = st.number_input("🧵 Texture Value (numeric):", min_value=0.0, max_value=1.0, value=0.0)
odor = st.number_input("👃 Odor Strength (numeric):", min_value=0.0, max_value=1.0, value=0.0)

# Prediction
if st.button("🔍 Predict Waste Type"):
    input_data = np.array([[weight, color, texture, odor]])
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)
    predicted_type = label_mapping[prediction[0]]  # Direct mapping without label encoder

    st.success(f"🗑 Predicted Waste Type: {predicted_type}")
