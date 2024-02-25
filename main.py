import streamlit as st
from rembg import remove
from  io import BytesIO
from PIL import Image
import base64


st.set_page_config(layout="wide",page_title="Image BG Remover")

st.write("## Remove Background from your image")
st.write(":dog: Try uploading an image to watch the background removed")

st.sidebar.write("## Upload and download")

MAX_FILE_SIZE=5*1024*1024


def convertImage(img):
    buf=BytesIO()
    img.save(buf,format="PNG")
    bytesIm=buf.getvalue()
    return bytesIm


def fixImage(upload):
    image=Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed=remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download fixed Image", convertImage(fixed),"fixed.png","image/png")

col1,col2=st.columns(2)
myUpload=st.sidebar.file_uploader("Upload an image",type=["png","jpg","jpeg"])

if myUpload is not None:
    if myUpload.size>MAX_FILE_SIZE:
        st.error("The uploaded file is too large")
    else :
        fixImage(upload=myUpload)
else :
    fixImage("/home/punith/usr-local/projects/bg-remover/main.jpg")






