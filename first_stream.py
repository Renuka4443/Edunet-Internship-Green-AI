import streamlit as st
import pandas as pd

st.write("Hello This is my first streamlit app")
df=pd.read_csv(r"E:\EDUNET GREEN AI\Salary_Data.csv")
st.write(df)
st.line_chart(df)