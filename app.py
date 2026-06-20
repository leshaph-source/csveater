import os

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from dotenv import load_dotenv

from agent.tools import (
    load_dataset,
    basic_eda
)

from agent.analyzer import (
    DataAnalyzer
)

load_dotenv()

st.set_page_config(
    page_title="AI Data Analyst",
    layout="wide"
)

st.title("AI Data Analyst")

st.write(
    "Загрузите CSV или Excel файл для анализа."
)

uploaded_file = st.file_uploader(
    "Выберите файл",
    type=["csv", "xlsx"]
)

if uploaded_file:

    save_path = uploaded_file.name

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    df = load_dataset(save_path)

    st.success("Файл успешно загружен")

    st.subheader("Первые строки")

    st.dataframe(df.head())

    if st.button("Запустить анализ"):

        with st.spinner("Выполняется анализ..."):

            report = basic_eda(df)

            analyzer = DataAnalyzer()

            result = analyzer.analyze(report)

        st.subheader("Результат анализа")

        st.markdown(result)

        numeric_cols = df.select_dtypes(
            include="number"
        ).columns

        if len(numeric_cols) > 1:

            st.subheader(
                "Корреляционная матрица"
            )

            fig, ax = plt.subplots(
                figsize=(10, 6)
            )

            sns.heatmap(
                df[numeric_cols]
                .corr(),
                annot=True,
                cmap="coolwarm",
                ax=ax
            )

            st.pyplot(fig)

        os.remove(save_path)
