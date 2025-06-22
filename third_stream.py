import streamlit as st
import pandas as pd

st.write("Hello This is my third streamlit app")
df=pd.read_csv(r"E:\EDUNET GREEN AI\solar_power_output(in).csv")
st.write(df)
st.line_chart(df)
