import streamlit as st
import joblib as jb
import numpy as np
salary=jb.load(r"E:\EDUNET GREEN AI\Energy_Consumption_predictor.pkl")
st.title("Welcome to the predict energy consumption model")
#input
temp=st.number_input("Temperature(0 to 35 °C):",min_value=0.0,max_value=35.0,value=5.0)

if st.button("Predict Energy Consumption"):
    new_input=np.array([[temp]])
    prediction=salary.predict(new_input)
    st.write(f"The expected energy consumption for temperature {temp}°C is {prediction[0]:,.6f} kWh")
    st.write("Thank you...........")
