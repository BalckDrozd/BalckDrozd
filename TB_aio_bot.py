from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db
from handlers import admin, client, other

async def on_startup(_):
    print('Бот готов к работе')
    sqlite_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
