from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command("help"))
async def help_command(message: Message):
    await message.answer("help command")
