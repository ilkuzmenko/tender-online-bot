from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command("help"))
async def main_menu(message: Message):
    await message.answer("help command")
