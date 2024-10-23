import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(layout="wide")
st.subheader("data chart")
upload1,upload2 = st.columns(2)

with upload1:
    upload_csv = st.file_uploader("upload csv file",type="csv")
if upload_csv:
    csv_file=pd.read_csv(upload_csv)
    with st.expander("read database"):
        st.table(csv_file)
    subject = csv_file.columns.tolist()
    subjectchoice = st.multiselect("subject upload",subject)
    subjectaverage = csv_file[subjectchoice].mean().reset_index()
    renamesubject = subjectaverage.rename(columns = {"index" : "subject",0:"average"})

    charttype = st.radio("type of chart",["bar chart","pie chart"],horizontal = True)
    if charttype == "bar chart":
        barchart = px.bar(renamesubject,x = "subject",y = "average")
        st.plotly_chart(barchart)
    
    if charttype == "pie chart":
        piechart = px.pie(renamesubject,names = "subject",values= "average")
        st.plotly_chart(piechart)

