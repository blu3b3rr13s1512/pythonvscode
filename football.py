import streamlit as st

st.title("Football Adventure")


st.header("Account Login")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username and password:
        st.success("Login successful!")
        
        
        st.header("Purchase Items")
        tickets = st.number_input("Number of Match Tickets ($100 each)", min_value=0, value=0)

        
        season_pass = st.selectbox("Select Season Pass", options=["Standard", "VIP"])

        
        st.subheader("Team Merchandise")
        merchandise_options = ['Jersey', 'Scarf', 'Hat']
        selected_merchandise = st.multiselect("Select Merchandise", options=merchandise_options)

        
        snack_options = ['Popcorn', 'Hotdog', 'Soda']
        selected_snacks = st.multiselect("Select Snacks", options=snack_options)

        
        premium_channel = st.selectbox("Select Premium Sports Channel Subscription", options=["Monthly", "Annual"])

        
        if st.button("Calculate Total Cost"):
            
            ticket_price = 100
            season_pass_prices = {'Standard': 200, 'VIP': 500}
            merchandise_prices = {'Jersey': 60, 'Scarf': 30, 'Hat': 20}
            snack_prices = {'Popcorn': 10, 'Hotdog': 15, 'Soda': 5}
            premium_channel_prices = {'Monthly': 20, 'Annual': 200}

           
            total_tickets = tickets * ticket_price
            total_season_pass = season_pass_prices[season_pass]

            
            total_merchandise = 0
            for item in selected_merchandise:
                total_merchandise += merchandise_prices[item]

           
            total_snacks = 0
            for item in selected_snacks:
                total_snacks += snack_prices[item]

            total_premium_channel = premium_channel_prices[premium_channel]

            
            total_cost = (total_tickets + total_season_pass + 
                          total_merchandise + total_snacks + 
                          total_premium_channel)

            st.success("The total cost of Liam's football adventure is: $",total_cost)
    else:
        st.error("Please enter both username and password!")