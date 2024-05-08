import streamlit as st

st.header("House Shop")

name = st.text_input("Enter your name: ")
salary =st.number_input("Enter your yearly salary: ")

if salary < 100000:
        st.write(name, "you can buy or rent an apartment.")
elif 100000 <= salary <= 500000:
        st.write(name, "you can buy a bungalow.")
elif 500000 < salary <= 1000000:
        st.write(name, "you can buy a duplex.")
elif 1000000 < salary <= 5000000:
        st.write(name, "you can buy a mansion.")
else:
        st.write(name, "you can buy an estate.")