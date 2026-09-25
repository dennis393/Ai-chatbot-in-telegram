from openrouter import OpenRouter
import sys
from openai import AsyncOpenAI
from config import settings

client = AsyncOpenAI(api_key=settings.OPENROUTER_TOKEN, base_url="https://openrouter.ai/api/v1")

user_input = input("message: ")

system_prompt = f"""
Сюда вы пишите либо роль ИИ, либо системные инструкции, в моем случае это обычный чат бот который работает по принципу ВОПРОС -> ОТВЕТ и все
""" 


response = client.chat.completions.create(
    model="nex-agi/nex-n2.5-pro:free",
    messages=[

            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
    ],
    temperature=0.7
)
sys.stdout.reconfigure(encoding='utf-8')
print(response.choices[0].message.content)