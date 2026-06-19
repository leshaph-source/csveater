from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

agent = create_pandas_dataframe_agent(
    ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    ),
    df,
    verbose=True,
    allow_dangerous_code=True
)
result = agent.invoke(
    "Проведи полный анализ датасета и найди инсайты"
)