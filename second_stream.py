import streamlit as st
import pandas as pd

st.write("Hello This is my second streamlit app")
df=pd.read_csv(r"E:\EDUNET GREEN AI\appliance_energy.csv")
st.write(df)
st.line_chart(df)
