from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp
from data_base import sqlite_db


class FSMAdmin(StatesGroup):
    name = State()


# Поиск по названию
@dp.message_handler(commands='НАйти_Фильм', state=None)
async def find_name(message: types.Message):
    await FSMAdmin.name.set()
    await message.reply('Введите название фильма')


# Ловим ответ
@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    name_film = message.text
    await sqlite_db.find_Film_name(message)
    await message.reply(f'Нашлось {await sqlite_db.find_Film_name(message)} совпадений')
    await state.finish()



async def echo_send(message: types.Message):
    pass


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(echo_send)
    # dp.register_message_handler(find_name, commands='НАйти_Фильм', state=None)
    # dp.register_message_handler(load_name, state=FSMAdmin.name)