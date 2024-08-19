import streamlit as st

initial_savings = 400

concert_cost = st.number_input("How much did you spend on the concert ticket? ")
dinner_cost = st.number_input("How much did you spend on dinner? ")
shopping_cost = st.number_input("How much did you spend on shopping? ")
transportation_cost = st.number_input("How much did you spend on transportation? ")
movie_cost = st.number_input("How much did you spend on the movie? ")

total_expenses = concert_cost + dinner_cost + shopping_cost + transportation_cost + movie_cost

amount_left = initial_savings - total_expenses

if amount_left > 0:
    investment_amount = amount_left // 4
    st.write("You have $",amount_left,"left", "and each investment will receive $",investment_amount)
elif amount_left == 0:
    st.write("You have no money left to invest.")
else:
    st.write("You spent $",amount_left,"more than your savings.")