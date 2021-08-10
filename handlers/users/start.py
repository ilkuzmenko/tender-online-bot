from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("start"))
async def main_menu(message: Message):
    await message.answer("Виберіть, будь ласка, зі списку", reply_markup=menu)
