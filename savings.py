import streamlit as st


firstsavings = 400

st.title("Savings Tracker")

concertcost = st.number_input("How much did you spend on the concert ticket?", min_value=0, step=1)
dinnercost = st.number_input("How much did you spend on dinner?", min_value=0, step=1)
shoppingcost = st.number_input("How much did you spend on shopping?", min_value=0, step=1)
transportationcost = st.number_input("How much did you spend on transportation?", min_value=0, step=1)
moviecost = st.number_input("How much did you spend on the movie?", min_value=0, step=1)


totalexpenses = concertcost + dinnercost + shoppingcost + transportationcost + moviecost


amountleft = firstsavings - totalexpenses


if amountleft > 0:
    investment_amount = amountleft / 4
    st.write("You have $",amountleft,"left. Each investment will get $",investment_amount)
elif amountleft == 0:
    st.write("You have no money left to invest.")
else:
    st.write("You spent more than your savings. You have no money left to invest.")