import streamlit as st
import pandas as pd
import seaborn as sns
@st.cache_data
df = sns.load_dataset('iris')
st.write(df)
st.write("Hello World ")
st.title("My title")
st.image("./images.jpg")

st.number_input("Pick a number", 0, 10)
st.date_input("Your birthday")
st.slider("Slide it:",0,100,25)


with st.sidebar:
    st.text_input("Filter by name")
    st.selectbox("Sort by", ["A-Z", "Z-A"])
    st.file_uploader("Upload a CSV")


# Load data