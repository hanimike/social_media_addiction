import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns 
import scipy as sp

st.title("Social Media Addiction")

    # Load Data
st.header("Load Data")
data = pd.read_csv("social_media_addiction.csv")

csv = data.to_csv(index=False)
st.download_button( label="Download dataset as CSV", 
                   data=csv, file_name="social_media_addiction.csv", mime="text/csv" )
     # Show Data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
st.dataframe(data)
    
    # Basic Info
st.header("\nInfo : ")
st.write(data.info())

st.header("\nShape of dataset:")
st.write(data.shape)

st.header("\nColumns names:")
st.write(data.columns)


st.header("First 5 rows:\n")
st.write(data.head())

st.header("\nLast 10 rows")
st.write(data.tail(10))

st.header("\nStatistical summary:\n")
st.write(data.describe())
