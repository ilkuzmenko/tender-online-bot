import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from middlewares.language import setup_middleware
from utils.mydb.Database import Database


loop = asyncio.get_event_loop()

bot = Bot(token=TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

i18n = setup_middleware(dp)
_ = i18n.gettext

db = Database()
loop.run_until_complete(db.create_pool())
