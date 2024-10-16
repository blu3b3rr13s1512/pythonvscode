import streamlit as st

st.title("Doctor Appointment Form")

n1,n2 = st.columns(2)

with n1:
    first = st.text_input("First name:")
with n2:
    last = st.text_input("Last name:")


phone = st.text_input("Phone Number:")

dob = st.date_input("Date of Birth:")

address = st.text_input("Street Address:")

address2 = st.text_input("Street Adress Line 2:")


p1,p2 = st.columns(2)

with p1:
    city = st.text_input("City:")

with p2:
    region = st.text_input("Region:")

zip = st.text_input("Postal / Zip code:")

email = st.text_input("Email:")

if st.button("Submit"):
    st.success("Submitted!")
    st.write(first,last,phone,dob,address,address2,city,region,zip,email)