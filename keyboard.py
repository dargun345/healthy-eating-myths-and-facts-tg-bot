from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

inline_keyboard = InlineKeyboardMarkup(inline_keyboard= [
                                                        [InlineKeyboardButton(text="1", callback_data="1")],
                                                        [InlineKeyboardButton(text="2", callback_data="2")]
                                                        ])


keyboard = ReplyKeyboardMarkup(keyboard=[
                                        [KeyboardButton(text="1")],
                                        [KeyboardButton(text="2")] 
                                        ])


begin = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Начать")]], resize_keyboard=True)


finish = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Закончить")]], resize_keyboard=True)