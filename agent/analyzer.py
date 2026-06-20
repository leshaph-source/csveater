import re
import os

from openai import OpenAI
from dotenv import load_dotenv

from agent.prompts import SYSTEM_PROMPT
from agent.tools import execute_python

load_dotenv()


class DataAgent:

    def __init__(self):

        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=os.getenv("NVIDIA_API_KEY")
        )

    def ask_llm(self, messages):

        response = self.client.chat.completions.create(
            model="deepseek-ai/deepseek-v4-pro",
            messages=messages,
            temperature=0.2,
            max_tokens=4096,
            extra_body={
                "chat_template_kwargs": {
                    "thinking": False
                }
            }
        )

        return response.choices[0].message.content

    def extract_code(self, text):

        match = re.search(
    r"<python>(.*?)</python>",
    text,
    re.DOTALL
)

        if match:
            return match.group(1).strip()

        return None

    def analyze(self, df):

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": """
Начни исследование датасета.
Выполняй код по необходимости.
"""
            }
        ]

        max_steps = 8

        for _ in range(max_steps):

            answer = self.ask_llm(messages)

            if "FINAL REPORT:" in answer:
                return answer

            code = self.extract_code(answer)

            if not code:
                return answer

            result = execute_python(code, df)

            messages.append({
                "role": "assistant",
                "content": answer
            })

            messages.append({
                "role": "user",
                "content":
                    f"Результат выполнения:\n{result}"
            })

        return "Лимит шагов анализа достигнут."
