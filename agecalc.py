import streamlit as st

st.title("My Age App")

name = st.text_input("Enter your name here")
year = st.number_input("What year is it now?")
yob = st.number_input("Enter your year of birth here",1950)
age = (year-yob)






if st.button("Check your age"):
    st.write(name,"you are",age,"years old.")