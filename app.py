import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader(
    "Загрузите CSV",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write(df.head())

    st.write("Размер:")
    st.write(df.shape)

    st.write("Описание:")
    st.write(df.describe())