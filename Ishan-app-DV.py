#header
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
from matplotlib import image



# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest1 = os.path.join(PARENT_DIR, "Datasets for ML")
dir_of_interest2 = os.path.join(PARENT_DIR, "Innomatics")

DATA_PATH= os.path.join(dir_of_interest1, "Classifier", "evilspirits.xlsx")
IMAGE_PATH = os.path.join(dir_of_interest2, "proj1", "ghosts.jpg")

st.title("Evil Spirit Explorer: Know about your favourite buri aatma!")
df = pd.read_excel(DATA_PATH)
st.dataframe(df)

img = image.imread(IMAGE_PATH)
st.image(img)



