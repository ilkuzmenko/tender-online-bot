from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp, _


@dp.message_handler(Command("help"))
async def help_command(message: Message):
    await message.answer(
        _("Є проблеми з моєю роботою?😳\n"
          "Звʼяжіться з підтримкою TenderOnline за "
          "<a href = \"https://tender-online.com.ua/contacts\">посиланням</a>."),
        parse_mode='HTML'
    )
