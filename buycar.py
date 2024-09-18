import streamlit as st

st.write("Welcome to the Car Buyer Program!")
name = st.text_input("What is your name? ")


salary = st.number_input(input("What is your yearly salary? "))


if salary < 30000:
    car_type = "used car"
elif salary >= 30000 and salary < 60000:
    car_type = "economy car"
elif salary >= 60000 and salary < 100000:
    car_type = "mid-range car"
elif salary >= 100000 and salary < 200000:
    car_type = "luxury car"
else:
    car_type = "supercar"


st.write(name,"based on your yearly salary of $",salary, "you can afford a",car_type)


