from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from loader import dp, db
from utils.db.comands import subscribe_user, get_blog_page


@dp.message_handler(Text(equals=["📩 Отримати новини"]))
async def btn_get_blog(message: Message):
    blog = await get_blog_page()
    await message.answer(blog, parse_mode='HTML')


@dp.message_handler(Text(equals=["✅Підписатися/❌Відписатися"]))
async def btn_subscribe(message: Message):
    if not bool(await db.fetchval('SELECT blog FROM users WHERE user_id = $1', message.from_user.id)):
        await subscribe_user(True, message.from_user.id)
        await message.answer("Ви успішно підписалися!")
    else:
        await subscribe_user(False, message.from_user.id)
        await message.answer("Ви успішно відпідписалися!")
