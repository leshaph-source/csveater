import json

from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

from agent.prompts import ANALYSIS_PROMPT


class DataAnalyzer:

    def __init__(self):

        self.llm = ChatOpenAI(
            model="gpt-4.1",
            temperature=0
        )

    def analyze(self, report):

        prompt = f"""
{ANALYSIS_PROMPT}

Статистика датасета:

{json.dumps(report, ensure_ascii=False, indent=2)}
"""

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return response.content
