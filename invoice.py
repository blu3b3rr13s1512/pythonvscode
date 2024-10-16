import streamlit as st

col1,col2 = st.columns(2)

    


with col1:
    col11, col12 = st.columns(2)
    with col11:
    
        st.image("kyra.png")
    st.write ("47 Hoi Ying Road, Lippo Centre Tower 1")
    st.write("Hong Kong, China")


co1,co2,co3 = st.columns(3)

with co1:
    st.write("Bill To:")
    customer = st.text_input('w', placeholder='Customer Name',label_visibility = 'collapsed')
    address = st.text_input('w', placeholder= 'Enter Email Address', label_visibility= 'collapsed')

with co2:
    st.write("Invoice#:")
    st.write ("Invoice Date:")
    st.write("Due Date:")

with co3:
    invno = st.text_input('w', placeholder = 'Invoice Number', label_visibility = 'collapsed')
    invdate = st.date_input ("invoice date:", label_visibility = 'collapsed')
    duedate = st.date_input ("due date:", label_visibility = 'collapsed')

p1,p2,p3,p4 = st.columns(4)

with p1:
    desc = st.text_input("Description:")

with p2:
    quan = st.number_input ("Quantity:",0)
with p3:
    price = st.number_input("Price/Unit")
with p4:
    calctotal = quan*price
    totalprice = st.number_input("TotalPrice",value=calctotal,disabled=True)



c1,c2 = st.columns(2)

with c1:
    st.write("Payment Info")
    st.write("Acc Name :",customer)
    st.write(" Acc Number : 12345678")
    st.write("Bank Name : UAE Bank")

with c2:
    duepayment = calctotal
    st.write("Payment Due:")
    st.subheader(f"$ {calctotal}")