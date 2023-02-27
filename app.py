import streamlit as st
from PIL import Image

st.title(":red[Innomatics] DataScience Internship")

image = Image.open(r'resources\images\internship.png')

st.image(image, caption='Datascience Intern')

st.header("Welcome to the India Biggest Free Internship Program by :red[Innomatics Research Labs]:sunglasses:")

btn_click = st.button("Click Me!👈")

if btn_click:
    st.balloons()