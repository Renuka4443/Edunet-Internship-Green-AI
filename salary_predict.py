import streamlit as st
import joblib as jb
import numpy as np
salary=jb.load(r"E:\EDUNET GREEN AI\Salary_predictor.pkl")
st.title("Welcome to the predict salary model")
#input
exp=st.number_input("Experiencce (0-45 years)",min_value=0.0,max_value=45.0,value=5.0)

if st.button("Predict Salary"):
    new_input=np.array([[exp]])
    prediction=salary.predict(new_input)
    st.write(f"The expected salary with {exp} years of experience is ${prediction[0]:,.2f}")
    st.write("Thank you...........")
