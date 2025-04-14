import random
from aiogram import *
from aiogram.filters import Command
import asyncio
from aiogram.types import *
from keyboard import *
import dotenv
import os

from config import *

dotenv.load_dotenv()
API_TOKEN = os.getenv("TOKEN")


bot = Bot(token=API_TOKEN)
dp = Dispatcher()

right_answer = ""
key = int()

@dp.message(Command("start"))
async def start_game(message: Message):
    
    await message.answer(text=f'🌟 Приветствуем вас в увлекательной игре! 🎉 "Угадай миф о здоровом питании"! Правила очень просты: вам нужно выбрать один из двух предложенных вариантов и отгадать, какой из них является мифом. Удачи! 🍀', reply_markup=begin) 

@dp.message(F.text == "Начать")
async def beg(message:Message):
    global right_answer
    
    random_key = random.choice(list(myths_dict.keys()))  
     
    current = myths_dict[random_key] 
    b = random.randint(0,1)
    a = str()
    c = str()
    if b == 0:
        a = 'myth'
        c = 'fact'
        right_answer = "2"
    else: 
        a = 'fact'
        c = 'myth'
        right_answer = "1"
    await message.answer(f"Выбирите где миф: \n\n1: {current[a]} \n2: {current[c]}", reply_markup=inline_keyboard)
    
    
@dp.callback_query(lambda callback_query: callback_query.data in ["1", "2"])
async def handle_response(callback:CallbackQuery):
    if (callback.data == "1" and right_answer == "1") or (callback.data == "2" and right_answer == "2"):
        await callback.answer("Вы выиграли! Ура!")
        
    else:
        await callback.answer("Вы проиграли.", )
    
    await callback.message.delete()
    await beg(callback.message)
    
    
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())