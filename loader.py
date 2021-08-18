import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from utils.db.Database import Database

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

loop = asyncio.get_event_loop()

bot = Bot(token=TOKEN, parse_mode="HTML")

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

db = Database()
loop.run_until_complete(db.connect())

