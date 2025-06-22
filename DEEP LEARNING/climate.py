import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import pickle

# Load the trained model (should predict Energy Consumption)
model = load_model('climate_prediction_model.h5')

# Load the scaler if you used one
# scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Energy Consumption Prediction")

st.write("### Enter the input features:")

# Input fields (10 features)
temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
rainfall = st.number_input("Rainfall")
wind_speed = st.number_input("Wind Speed")
solar_radiation = st.number_input("Solar Radiation")
pressure = st.number_input("Pressure")
population_density = st.number_input("Population Density")
industrial_activity_index = st.number_input("Industrial Activity Index")
green_cover = st.number_input("Green Cover")
air_quality_index = st.number_input("Air Quality Index")

if st.button("Predict"):
    input_data = np.array([[temperature, humidity, rainfall, wind_speed, solar_radiation,
                            pressure, population_density, industrial_activity_index,
                            green_cover, air_quality_index]])

    # If you used a scaler, uncomment this:
    # input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)
    st.success(f"Predicted Energy Consumption: {prediction[0][0]}")