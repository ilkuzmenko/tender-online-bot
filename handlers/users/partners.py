from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message
from data.text_const import low_help, analytics_help
from keyboards.default import partners
from loader import dp


@dp.message_handler(Command("partners"))
async def partners_command(message: Message):
    await message.answer("Виберіть, будь ласка, зі списку", reply_markup=partners)


@dp.message_handler(Text(equals=["⚖️ Правова підтримка"]))
async def btn_partners1(message: Message):
    await message.answer(low_help, parse_mode='HTML')


@dp.message_handler(Text(equals=["📈 Аналітика ринку"]))
async def btn_partners2(message: Message):
    await message.answer(analytics_help, parse_mode='HTML')
