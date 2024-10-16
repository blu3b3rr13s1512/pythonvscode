import streamlit as st


st.title("Church Member Registration")


name = st.text_input("Member Name")
age = st.number_input("Age")
gender = st.radio("Gender", options=["Male", "Female"])


if st.button("Submit"):
    
    if age < 13:
        category = "Child"
    elif 13 <= age < 20:
        category = "Teen"
    elif 20 <= age < 65:
        category = "Adult"
    else:
        category = "Senior"
    
    
    st.write ( "Member:",name, "Age:",age, "Gender:", gender, "Category:", category)