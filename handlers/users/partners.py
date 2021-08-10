from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from data.text_const import low_help, analytics_help
from loader import dp


@dp.message_handler(Text(equals=["⚖️ Правова підтримка"]))
async def btn_partners1(message: Message):
    await message.answer(low_help, parse_mode='HTML')


@dp.message_handler(Text(equals=["📈 Аналітика ринку"]))
async def btn_partners2(message: Message):
    await message.answer(analytics_help, parse_mode='HTML')
