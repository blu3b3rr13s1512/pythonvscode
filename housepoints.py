import streamlit as st
import pandas as pd
import os


csv_file = 'house_points.csv'


if 'house_points' not in st.session_state:
    st.session_state.house_points = {
        "Nightingale": 0,
        "Rowell": 0,
        "Crozier": 0,
        "Upsdell": 0
    }
    st.session_state.submitted = False


if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        st.session_state.house_points[row['House']] = row['Points']


def save_to_csv():
    df = pd.DataFrame(list(st.session_state.house_points.items()), columns=['House', 'Points'])
    df.to_csv(csv_file, index=False)


def display_house_points():
    st.write("### House Points")
    for house, points in st.session_state.house_points.items():
        st.write(f"{house}: {points} points")


st.title("House Points for Recycling")

username = st.text_input("Enter your Lionel username:")


house = st.selectbox("Select a house:", list(st.session_state.house_points.keys()))


recycled_item = st.text_input("What did you recycle?")


if st.button("Add House Point"):
    if not st.session_state.submitted:
        if recycled_item and username:
            
            st.session_state.house_points[house] += 1
            
            
            st.success(f"1 house point added to {house} for recycling {recycled_item} by {username}!")


            st.session_state.submitted = True
            
            
            save_to_csv()
        else:
            st.error("Please enter what you recycled and your username.")
    else:
        st.warning("You have already submitted a point for this session.")


display_house_points()