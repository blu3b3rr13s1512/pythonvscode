import streamlit as st
import pandas as pd
import os

# File path for the CSV
csv_file = 'house_points.csv'

# Initialize session state for house points if not already done
if 'house_points' not in st.session_state:
    st.session_state.house_points = {
        "Nightingale": 0,
        "Rowell": 0,
        "Crozier": 0,
        "Upsdell": 0
    }
    st.session_state.submitted = False

# Load existing data from CSV if it exists
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        st.session_state.house_points[row['House']] = row['Points']

# Function to save house points to CSV
def save_to_csv():
    df = pd.DataFrame(list(st.session_state.house_points.items()), columns=['House', 'Points'])
    df.to_csv(csv_file, index=False)

# Function to display house points
def display_house_points():
    st.write("### House Points")
    for house, points in st.session_state.house_points.items():
        st.write(f"{house}: {points} points")

# Streamlit app
st.title("House Points for Recycling")

# Input for Lionel username
username = st.text_input("Enter your Lionel username:")

# Select house
house = st.selectbox("Select a house:", list(st.session_state.house_points.keys()))

# Input for what was recycled
recycled_item = st.text_input("What did you recycle?")

# Button to add house point
if st.button("Add House Point"):
    if not st.session_state.submitted:
        if recycled_item and username:
            # Increment the house points
            st.session_state.house_points[house] += 1
            
            # Show success message
            st.success(f"1 house point added to {house} for recycling {recycled_item} by {username}!")

            # Mark as submitted to prevent further submissions
            st.session_state.submitted = True
            
            # Save the updated points to CSV
            save_to_csv()
        else:
            st.error("Please enter what you recycled and your username.")
    else:
        st.warning("You have already submitted a point for this session.")

# Display current house points
display_house_points()