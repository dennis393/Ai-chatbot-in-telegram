import asyncio
from aiogram import Bot, Dispatcher, F
from config import settings
from aiogram.filters import CommandStart, Command 
from aiogram.types import Message
from orm_from_llm import chatHistory, LongMemory, async_session
from sqlalchemy import select
dp = Dispatcher()

#Основная функция для запуска бота
async def main():
    token = settings.TG_TOKEN          
    if not token:                       
        error = "No token provided"      
        raise ValueError(error)          
    bot = Bot(token=token)               
    print("Starting bot...")
    try:
        await dp.start_polling(bot)    
    finally:
        print("Bot stopped")
    
@dp.message(CommandStart())
async def hi_func(message: Message):
    user_id = message.from_user.id
    if user_id != settings.MY_TG_ID:
        await message.answer("Вы не можете пользоваться этим ботом")
        return
    await message.answer("Привет я Ася, я переехала в телеграм теперь мы можем общаться в здесь")

#Через команду заносим данные которые надо чтобы ии помнил всегда
@dp.message(Command("remember this")) 
async def remember_long_time(message: Message):
    user_id = message.from_user.id
    async with async_session() as sess:
        if message.from_user.id != settings.MY_TG_ID:
            return
        if not command.args:
            await message.answer("После команды /remember ничего нет, укажи")
            return
        sess.add(LongMemory(category="user", fact=command.args))
        await sess.commit()
    await message.answer("Запомнила")
    
#Сохраняем сообщения в память бота    
async def save_message(role: str, content: str):
    async with async_session() as sess:
        sess.add(chatHistory(role=role, content=content))
        await sess.commit()
        
#Поднимаем последние 30 собщений чтобы ИИ был в курсе диалога
async def get_30_last_messages(limit=30):
    async with async_session() as sess:
        res = await sess.execute(select(chatHistory).order_by(chatHistory.id.desc()).limit(limit))
        messages = res.scalars().all()
        return [{"role": m.role, "content": m.content} for m in reversed(messages)]
    
#Возвращаем все факты из долгой памяти ИИ
async def get_all_facts():
    async with async_session() as sess:
        res = await sess.execute(select(LongMemory))
        messages = res.scalars().all()
        return [x.fact for x in messages]

@dp.message(F.text & ~F.text.startswith("/")) #Условие означает что хендлер сработает только на сообщения, где есть текст (F.text) и текст не начинается с / (~ означает «не»).
async def chat(message: Message):
    if message.from_user.id != settings.MY_TG_ID:
        return

    await save_message("user", message.text)
    history = await get_30_last_messages(30)
    facts = await get_all_facts()
    answer = await ask_llm(history, facts)
    await save_message("assistant", answer)
    await message.answer(answer)    
    


    
    


if __name__ == '__main__':
    asyncio.run(main())