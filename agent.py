from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

def analyze_dataframe(df):

    info = f"""
Размер датасета: {df.shape}

Столбцы:
{list(df.columns)}

Первые строки:
{df.head(10).to_string()}

Описание:
{df.describe(include='all').to_string()}
"""

    prompt = f"""
Проведи анализ датасета.

{info}

Укажи:

1. Общую характеристику данных.
2. Основные закономерности.
3. Возможные аномалии.
4. Интересные инсайты.
5. Практические выводы.
"""

    response = llm.invoke(prompt)

    return response.content
