from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command("help"))
async def help_command(message: Message):
    await message.answer(f"Є проблеми з моєю роботою?😳\n"
                         f"Звʼяжіться з підтримкою TenderOnline за "
                         f"<a href = \"https://tender-online.com.ua/contacts\">посиланням</a>.",
                         parse_mode='HTML')
