#  Create a student scores database which can 
#  -get the name of the student
#  -get 4 subjects score
#  -calculate the average of the subjects
#  -calculate the grade (A,B,C,D,E,F) using the average
#  -update your csv file
# What is a CSV file?
# A CSV file is a text file that each data is seperated by a comma (comma seperated values)

import streamlit as st
import pandas as pd #pandas help to open, read, and display CSV files as a table (dataframe)

st.set_page_config(layout = 'wide') # this makes our page full width

st.header("Student's Scores Database")

df = pd.read_csv('scores.csv') # here pandas will read the csv file  
st.table(df)#here streamlit will display it as a table (dataframe)

inputname = st.text_input("Student name:")
engscorecol,matscorecol = st.columns(2)
with engscorecol:
    engscore = st.number_input("Student's score in English:",0)
with matscorecol:
    matscore = st.number_input("Student's score in Maths:",0)

sciscorecol,medscorecol = st.columns(2)
with sciscorecol:
    sciscore = st.number_input ("Student's score in Science:",0)
with medscorecol:
    medscore = st.number_input ("Student's score in Media:",0)
totalscore = (engscore + matscore+sciscore+medscore)


average = totalscore/4
if average >= 90:
    grade = "A+"
elif average >=80:
    grade = "A"
elif average >=70:
    grade = "B"
elif average >=60:
    grade = "C"
elif average >=50:
    grade = "D"
elif average <50:
    grade = "F"

if st.button ("Check your overall score:"):
    st.write (f"Your total score is {totalscore} and your average is {average} and your grade is {grade}")
    studentsdict = {'Name':[inputname],'Math':[matscore],'English':[engscore],'Science':[sciscore],'Media':[medscore]}
    st.write(studentsdict)
    table = pd.DataFrame(studentsdict)
    st.table(table)


    