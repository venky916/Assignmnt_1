import streamlit as st
from PIL import Image

st.title("My Profile :wave:")

col1, col2 = st.columns(2)

image = Image.open(r'resources\images\iron_man.jpg')

col1.image(image, caption='')

with col2:
    st.header("Maliga Venkatesh")
    st.write("Python_Programmer|Front_end web_developer| Data_Scientist  ")
    

st.markdown(":e-mail: venkateshsmsv1999@gmail.com")
st.text('')
im = Image.open(r'C:\Users\sudee\Desktop\dataScience_internship\assignment_1\resources\images\linkedin.png')
st.image(im,use_column_width="never")
st.markdown("linkedin <https://www.linkedin.com/in/venkatesh-maliga-6a28a3249/>")
st.text('')
im_1 = Image.open(r'C:\Users\sudee\Desktop\dataScience_internship\assignment_1\resources\images\github.png')
st.image(im_1)
st.write("Github <https://github.com/venky916>")

st.write("Currently studying final year in **Priyadarshini college of engineering and technology** at __Nellore__  ")
st.write("This is my first datascience internship and I am very excited for being part of it and looking forward to learn more intresting things  ")
