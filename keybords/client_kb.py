from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Поиск_по_названию')
b2 = KeyboardButton('/Поиск_по_описанию')
b3 = KeyboardButton('/Случайный')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2).add(b3)
