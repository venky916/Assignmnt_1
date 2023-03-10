import streamlit as st
from PIL import Image
from matplotlib import image
import os



st.title(":red[Innomatics] DataScience Internship")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path of directory_of_interest
dir_of_interest = os.path.join(FILE_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "internship.png")

img = image.imread(IMAGE_PATH)
st.image(img,caption='Datascience Intern')


st.header("Welcome to the India Biggest Free Internship Program by :red[Innomatics Research Labs]:sunglasses:")

btn_click = st.button("Click Me!👈")

if btn_click:
    st.balloons()