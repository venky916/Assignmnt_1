import streamlit as st
from PIL import Image
from matplotlib import image
import os


st.title("My Profile :wave:")

col1, col2 = st.columns(2)

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH_1 = os.path.join(dir_of_interest, "images", "iron_man.jpg")
#image = Image.open(r'resources\images\iron_man.jpg')
#col1.image(IMAGE_PATH, caption='')

img = image.imread(IMAGE_PATH_1)
col1.image(img,use_column_width="auto")

with col2:
    st.header("Maliga Venkatesh")
    st.write("Python_Programmer|Front_end web_developer| Data_Scientist  ")
    

st.markdown(":e-mail: venkateshsmsv1999@gmail.com")
st.text('')
# im = Image.open(r'C:\Users\sudee\Desktop\dataScience_internship\assignment_1\resources\images\linkedin.png')
# st.image(im,use_column_width="never")
IMAGE_PATH_2 = os.path.join(dir_of_interest, "images", "linkedin.png")
img = image.imread(IMAGE_PATH_2)
st.image(img,use_column_width="auto")


st.markdown("linkedin <https://www.linkedin.com/in/venkatesh-maliga-6a28a3249/>")
st.text('')
# im_1 = Image.open(r'C:\Users\sudee\Desktop\dataScience_internship\assignment_1\resources\images\github.png')
# st.image(im_1)
IMAGE_PATH_3 = os.path.join(dir_of_interest, "images", "github.png")
img = image.imread(IMAGE_PATH_3)
st.image(img,use_column_width="auto")

st.write("Github <https://github.com/venky916>")

st.write("Currently studying final year in **Priyadarshini college of engineering and technology** at __Nellore__  ")
st.write("This is my first datascience internship and I am very excited for being part of it and looking forward to learn more intresting things  ")
