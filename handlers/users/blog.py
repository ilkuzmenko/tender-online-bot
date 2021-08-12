from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from loader import dp, db
from utils.db.comands import subscribe_user


@dp.message_handler(Text(equals=["📩 Отримати новини"]))
async def btn_tariff1(message: Message):
    await message.answer("Функціонал в розробці", parse_mode='HTML')


@dp.message_handler(Text(equals=["✅Підписатися/❌Відписатися"]))
async def btn_tariff1(message: Message):
    if not bool(await db.fetchval('SELECT blog FROM users WHERE user_id = $1', message.from_user.id)):
        await subscribe_user(True, message.from_user.id)
        await message.answer("Ви успішно підписалися!")
    else:
        await subscribe_user(False, message.from_user.id)
        await message.answer("Ви успішно відпідписалися!")
