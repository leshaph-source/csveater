from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="deepseek/deepseek-chat-v3-0324:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
),
    df,
    verbose=True,
    allow_dangerous_code=True
)
result = agent.invoke(
    "Проведи полный анализ датасета и найди инсайты"
)
