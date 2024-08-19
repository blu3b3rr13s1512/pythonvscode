import streamlit as st
st.subheader(':pink[Enter Student Chinese Scores]')
g1,g2 = st.columns([2,1])
with g1:
    name = st.text_input("Enter the Student's Name:")
with g2:
    grade = st.selectbox("Please choose your grade", ['Grade 1','Grade 2','Grade 3','Grade 4','Grade 5','Grade 6'])

sub1,sub2 = st.columns(2)

with sub1:
    math = st.number_input("Please enter student Math score",0,100,step=10)
    art = st.number_input("Please enter student Art Score",0,100,step=10)
    comp = st.number_input("Please enter student Computer score",0,100,step=10)

with sub2:
    eng = st.number_input("Please enter student English score",0,100,step=10)
    sci = st.number_input(" please enter student Science score",0,100,step=10)
    french = st.number_input("Please enter student French Score",0,100,step=10)

#homework: 