import pandas as pd
import streamlit as st
import plotly.express as px

from agent import analyze_dataframe

st.set_page_config(
    page_title="AI Data Analytics",
    layout="wide"
)

st.title("📊 AI Data Analytics Dashboard")

uploaded_file = st.file_uploader(
    "Загрузите CSV",
    type=["csv"]
)

if uploaded_file:

    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("Предпросмотр данных")
        st.dataframe(df.head())

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Строк", df.shape[0])

        with col2:
            st.metric("Столбцов", df.shape[1])

        st.subheader("Описание данных")
        st.dataframe(df.describe(include="all"))

        numeric_cols = df.select_dtypes(include="number").columns

        if len(numeric_cols) > 0:

            st.subheader("Визуализация")

            selected_col = st.selectbox(
                "Выберите числовой столбец",
                numeric_cols
            )

            fig = px.histogram(
                df,
                x=selected_col,
                title=f"Распределение: {selected_col}"
            )

            st.plotly_chart(fig, use_container_width=True)

        st.divider()

        st.subheader("🤖 AI-анализ датасета")

        if st.button("Запустить AI-анализ"):

            with st.spinner("Анализируем данные..."):

                report = analyze_dataframe(df)

            st.success("Анализ завершён")

            st.markdown(report)

    except Exception as e:
        st.error(f"Ошибка: {e}")
