import streamlit as st

menu = st.sidebar.selectbox('Choose an option',['Upload Image','Upload Audio','Upload Video'])

if menu == 'Upload Image':
    selectoption = st.radio('Choose option',['Upload a Picture','Take a Picture'],horizontal=True)
    uploadimage = st.file_uploader("Upload your image here", type=["jgp","jpeg","png"])
    if uploadimage:
        st.image(uploadimage)
if selectoption == 'Take a Picture':
    camera = st.camera_input("Smile to the camera!")

if menu == 'Upload Audio':
    uploadaudio = st.file_uploader("Upload your audio here", type = ['mp3','wav'])
    if uploadaudio:
        st.audio(uploadaudio,format='audio/mp3')

if menu =='Upload Video':
    youtubelink = st.text_input("Paste in your YouTube Link Here")
    if st.button("Play your Youtube Video"):
        st.video(youtubelink)
    else:
        st.info("Please paste your link first")