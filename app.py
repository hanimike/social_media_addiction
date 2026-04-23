
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns 
import scipy as sp
   # Title

st.title("Social Media Addiction Analysis")

st.markdown("""
### Project Description
This interactive app analyzes how **social media usage** affects **addiction, mental health, productivity, and FOMO (fear of missing out)**.  

The dataset includes participants' daily usage time, addiction levels, mental health scores, and productivity loss.  
Through **data cleaning, statistical summaries, and visualizations**, the app highlights key insights such as:
- How increased usage relates to higher addiction levels
- The impact of usage on mental health and productivity
- Gender differences in usage 
- Correlations between FOMO and addiction

This project combines raw data exploration with engaging charts to tell a clear story about digital habits.
""")

    # Load Data
st.header("Load Data")
data = pd.read_csv("social_media_addiction.csv")

csv = data.to_csv(index=False)
st.download_button(
    label="Download dataset as CSV", 
    data=csv, 
    file_name="social_media_addiction.csv", 
    mime="text/csv")

# Show Data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
st.dataframe(data)
    
    # Basic Info
st.header("Info:")
st.write(data.info())


st.header("Dataset Shape")
st.write(data.shape)

st.header("Column Names")
st.write(data.columns)

st.header("First 5 Rows")
st.write(data.head())

st.header("Last 10 Rows")
st.write(data.tail(10))

st.header("Statistical Summary")
st.write(data.describe())

st.header("Data Cleaning")
data.columns = data.columns.str.lower().str.replace(" ", "_")
st.write(data.columns)

st.header("Checking Missing Values")
st.write("\nMissing Values:\n", data.isnull().sum())

st.subheader("Handling Missing Values")
data = data.dropna()
st.write(data)

st.subheader("Checking & Removing Duplicates ")
st.write("Duplicate Rows:", data.duplicated().sum())
data= data.drop_duplicates()
st.dataframe(data)

st.header("Usage Level")

data["usage_level"] = pd.cut(
    data["daily_usage_time_min"],
    bins=[0, 60, 180, 300],
    labels=["Low", "Medium", "High"])

st.write(data[["daily_usage_time_min", "usage_level"]].head())

st.subheader("Analysing Usage , Addiction and Mental Health")
st.write("Average Daily Usage:", data["daily_usage_time_min"].mean())
st.write("Maximum Addiction Level:", data["addiction_level"].max())
st.write("Average Mental Health Score:", data["mental_health_index"].mean())

st.subheader("Average Usage by Gender")
avg_usage = data.groupby("gender")["daily_usage_time_min"].mean()
st.write(avg_usage)

st.subheader("Bar Chart :  Usage by Gender")
plt.figure(figsize=(6,4))
data.groupby("gender")["daily_usage_time_min"].mean().plot(kind="bar")
plt.title("Average Social Media Usage by Gender")
plt.xlabel("Gender")
plt.ylabel("Usage Time")
st.pyplot(plt)

st.subheader("Scatter Plot :  Usage Vs Addiction")
plt.figure(figsize=(6,4))
order = ["Low", "Moderate", "Severe", "High"]
data["addiction_level"] = pd.Categorical(data["addiction_level"], categories=order, ordered=True)
sns.scatterplot(x="daily_usage_time_min", y="addiction_level", data=data)
plt.title("Daily Usage Time vs Addiction Level")
st.pyplot(plt)

st.subheader("Scatter Plot :  Usage Vs Mental Health")
plt.figure(figsize=(6,4))
sns.scatterplot(x="daily_usage_time_min", y="mental_health_index", data=data)
plt.title("Usage Time vs Mental Health")
st.pyplot(plt)

st.subheader("Box Plot:  Addiction By Gender")
order = ["Low", "Moderate", "Severe", "High"]
data["addiction_level"] = pd.Categorical(
    data["addiction_level"], categories=order, ordered=True)
fig = px.box(
    data,
    x="gender",
    y="addiction_level",
    color="gender",
    title="Addiction Levels by Gender",
    category_orders={"addiction_level": order})
st.plotly_chart(fig)

st.subheader("Histogram :  Usage Distribution")
fig = px.histogram(data,
                   x="daily_usage_time_min",
                   nbins=20,
                   title="Distribution of Daily Usage Time")

st.plotly_chart(fig)

st.subheader("Heat Map :  Correlation Matrix")
plt.figure(figsize=(10,6))
corr = data.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Between Variables")
st.pyplot(plt)

st.subheader("Scatter Plot :  Fomo Vs Addiction")
fig = px.scatter(
    data,
    x="fomo_score",
    y="addiction_level",
    color="gender",
    size="daily_usage_time_min",
    title="FOMO vs Addiction with Usage Insight",
    category_orders={"addiction_level": order} )
st.plotly_chart(fig)

st.subheader("Scatter plot : Productivity Vs  Usage")
fig = px.scatter(data,
                 x="daily_usage_time_min",
                 y="productivity_loss_score",
                 trendline="ols",
                 title="Usage vs Productivity")

st.plotly_chart(fig)

st.subheader("Scatter plot : Daily Usage vs Mental Health ")
fig = px.scatter(data,
                 x="daily_usage_time_min",
                 y="mental_health_index",
                 color="gender",
                 trendline="ols",
                 title="Usage vs Mental Health")

st.plotly_chart(fig)

