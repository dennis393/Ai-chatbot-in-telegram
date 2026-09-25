import asyncio
from aiogram import Bot, Dispatcher
from config import settings
from aiogram.filters import CommandStart, Command 
from aiogram.types import Message

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
    await message.answer("Привет я Ася, я переехала в телеграм теперь мы можем общаться в здесь")



if __name__ == '__main__':
    asyncio.run(main())