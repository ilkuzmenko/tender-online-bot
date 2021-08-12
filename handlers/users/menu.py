from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message
from keyboards.default import menu, faq, tariff, partners, blog
from data.text_const import chef_answer, about_prozorro
from loader import dp


@dp.message_handler(Command("menu"))
async def help_command(message: Message):
    await message.answer("Виберіть, будь ласка, зі списку", reply_markup=menu)


@dp.message_handler(Text(equals=["🔙 Головне меню"]))
async def back_to_menu(message: Message):
    await message.answer("Виберіть, будь ласка, зі списку", reply_markup=menu)


@dp.message_handler(Text(equals=["📎 Блог"]))
async def subscribe(message: Message):
    await message.answer("Виберіть, будь ласка, зі списку", reply_markup=blog)


@dp.message_handler(Text(equals=["🔎 Пошук"]))
async def search(message: Message):
    await message.answer("Функціонал в розробці")


@dp.message_handler(Text(equals=["🆘 FAQ"]))
async def faq_menu(message: Message):
    await message.answer("Виберіть, будь ласка, зі списку", reply_markup=faq)


@dp.message_handler(Text(equals=["💰 Тарифи"]))
async def tariff_menu(message: Message):
    await message.answer("Виберіть, будь ласка, зі списку", reply_markup=tariff)


@dp.message_handler(Text(equals=["⭐️ Написати керівнику"]))
async def chef_help(message: Message):
    await message.answer(chef_answer, parse_mode='HTML')


@dp.message_handler(Text(equals=["🔵 Про Prozorro"]))
async def prozorro_about(message: Message):
    await message.answer(about_prozorro, parse_mode='HTML')


@dp.message_handler(Text(equals=["🤝 Партнерські послуги"]))
async def partners_menu(message: Message):
    await message.answer("Виберіть, будь ласка, зі списку", reply_markup=partners)
