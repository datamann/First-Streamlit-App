import pandas as pd
import streamlit as st
from PIL import Image

st.title("File Uploading")

#Image
st.subheader("1.Uploading an Image")
img_file = st.file_uploader("Upload an image",type=["png","jpg","jpeg"])
if img_file is not None:
    
    file_det_img = {"file name":img_file.name,"file type":img_file.type,"file size":img_file.size}
    st.write(file_det_img)
    
    st.image(Image.open(img_file))                    #to display uploaded file

#Audio
st.subheader("2.Uploading an Audio")
audio_file = st.file_uploader("Upload an audio file",type=["wav","mp3"])
if audio_file is not None:
    
    file_det_audio = {"file name":audio_file.name,"file type":audio_file.type,"file size":audio_file.size}
    st.write(file_det_audio)
    
    st.audio(audio_file)

#Video
st.subheader("3.Uploading a Video")
video_file = st.file_uploader("Upload a video file",type=["mp4","mov"])
if video_file is not None:
    
    file_det_video = {"file name":video_file.name,"file type":video_file.type,"file size":video_file.size}
    st.write(file_det_video)
    
    st.video(video_file)

