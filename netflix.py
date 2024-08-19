import streamlit as st
import pandas as pd
password = "55651512"
#st.sidebar.header 
movies_df = pd.read_csv
st.sidebar.header("Login")
loginpasswork = st.sidebar.text_input("Password", type ="password")
loginbutton = st.sidebar.button("Login")

st.write("Browse Movies")

genre = st.sidebar.selectbox("Select Genre",["All"], + list(movies_df))