from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from create_bot import dp
import sqlite3


class FSMAdmin(StatesGroup):
    name = State()


# Поиск по названию
@dp.message_handler(commands='Поиск_по_названию', state=None)
async def find_name(message: types.Message):
    await FSMAdmin.name.set()
    await message.reply('Введите название фильма')


# Ловим ответ
@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    name_film = message.text
    await message.reply(f'Вы ищите фильм {name_film}')
    await state.finish()

    db = sqlite3.connect('BD_Film_lordfilm.db')
    print(db)
    cur = db.cursor()
    print(cur)

    name_list = []
    year_list = []
    kp_rate_list = []
    imdb_rate_list = []
    link_film_list = []
    link_img_list = []
    opisanie_list = []

    f= cur.execute("SELECT * FROM BDFilm").fetchall()
    print(f)
    # for name in cur.execute('SELECT NAME FROM BDFilm WHERE NAME LIKE ?', ('%' + name_film + '%',)):
    #     print(name)
    #     print(name[0])
        # name_list.append(name[0])

