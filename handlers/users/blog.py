import logging

from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from aiogram.utils.exceptions import MessageNotModified, MessageTextIsEmpty

from keyboards.inline import blog_scroll
from loader import dp, db
from utils.mydb.comands import get_blog_page


user_data = {}


@dp.message_handler(Text(equals=["📩 Отримати новини"]))
async def btn_get_blog(message: Message):
    blog_page = await get_blog_page(0)
    await message.answer(blog_page, parse_mode='HTML', reply_markup=blog_scroll, disable_web_page_preview=True)


async def update_text(message: Message, new_value: int):
    blog_page = await get_blog_page(new_value)
    try:
        await message.edit_text(blog_page, parse_mode='HTML', reply_markup=blog_scroll, disable_web_page_preview=True)
    except MessageTextIsEmpty:
        logging.info("News MessageTextIsEmpty")
    except MessageNotModified:
        logging.info("News MessageNotModified")


@dp.callback_query_handler(Text(startswith="blog_"))
async def callbacks_num(call: CallbackQuery):
    first_page = user_data.get(call.from_user.id, 0)
    action = call.data.split("_")[1]

    if action == "incr":
        user_data[call.from_user.id] = first_page + 1
        await update_text(call.message, first_page + 1)
    elif action == "decr":
        user_data[call.from_user.id] = first_page - 1
        await update_text(call.message, first_page - 1)
    elif action == "finish":
        await call.message.edit_text(first_page)
    await call.answer()


@dp.message_handler(Text(equals=["✅ Підписатися/❌ Відписатися"]))
async def btn_subscribe(message: Message):
    async with db.connection.cursor() as cursor:
        await cursor.execute(f"SELECT blog FROM users WHERE user_id = {message.from_user.id}")
        status = int(''.join(map(str, await cursor.fetchone())))
        if status == 0:
            await cursor.execute(f"UPDATE users SET blog = 1 WHERE user_id = {message.from_user.id}")
            await message.answer("✅ Ви успішно підписалися!")
        else:
            await cursor.execute(f"UPDATE users SET blog = 0 WHERE user_id = {message.from_user.id}")
            await message.answer("❌ Ви успішно відпідписалися!")
