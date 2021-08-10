from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from data.text_const import tariff_prozorro, tariff_prozorro_market
from loader import dp


@dp.message_handler(Text(equals=["🔵 Prozorro"]))
async def btn_tariff1(message: Message):
    await message.answer(tariff_prozorro, parse_mode='HTML')


@dp.message_handler(Text(equals=["🟢 Prozorro Market"]))
async def btn_tariff2(message: Message):
    await message.answer(tariff_prozorro_market, parse_mode='HTML')
