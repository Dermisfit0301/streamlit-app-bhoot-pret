
from chart_studio import plotly as pl
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
dir_of_interest = os.path.join(PARENT_DIR, "resource")

IMAGE_PATH = os.path.join(dir_of_interest, "image", "ghosts.jpg")
DATA_PATH= os.path.join(dir_of_interest, "dataset", "evilspirits.xlsx")

st.markdown("# Main page ")
st.sidebar.markdown("# Main page ")
st.title(":red[Evil Spirit Explorer: Know about your favourite buri aatma!]")
st.header(":green[Warning]: Dear faint hearted,please stay Away")
img = image.imread(IMAGE_PATH)
st.image(img)

st.markdown("# haunted page ")
st.sidebar.markdown("# haunted page ")
df = pd.read_excel(DATA_PATH)
st.dataframe(df)

type = st.selectbox("Select the buri aatma:", df['type'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['type'] == type], x="bone_length")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.bar(df[df['type']  == type], y="rotting_flesh")
col2.plotly_chart(fig_2, use_container_width=True)



