from openrouter import OpenRouter
import sys
from openai import AsyncOpenAI
from config import settings

client = AsyncOpenAI(api_key=settings.OPENROUTER_TOKEN, base_url="https://openrouter.ai/api/v1")


system_prompt ="""
Действуй как  Senior Python разработчик. 
Отвечай строго по делу, максимально тезисно, без лишних вступлений, вежливости и "воды". Пиши только факты.
""" 

async def llm_ans(history, facts):
    system = system_prompt
    if facts: #Добавялем факты из LongMemory в промпт
        
        system += "\n\nЧто ты знаешь обо мне:\n" + "\n".join(facts)
   
    response = await client.chat.completions.create(
        
    model="openrouter/free",
    
    messages=[{"role": "system", "content": system}] + history,
    
    temperature=0.7,
    )
    return response.choices[0].message.content