import logging

from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from aiogram.utils.exceptions import MessageTextIsEmpty, MessageNotModified, MessageCantBeEdited

from keyboards.inline import news_scroll
from loader import dp, db
from utils.mydb.comands import get_news_page

user_data = {}


@dp.message_handler(Text(equals=["📩 Отримати новини"]))
async def btn_get_news(message: Message, new_value=0):
    news_page = await get_news_page(new_value)
    try:
        await message.edit_text(news_page, parse_mode='HTML', reply_markup=news_scroll, disable_web_page_preview=True)
    except MessageCantBeEdited:
        await message.answer(news_page, parse_mode='HTML', reply_markup=news_scroll, disable_web_page_preview=True)
    except MessageTextIsEmpty or MessageNotModified:
        logging.info("News MessageTextIsEmpty or MessageNotModified")


@dp.callback_query_handler(Text(startswith="news_"))
async def callbacks_num(call: CallbackQuery):
    first_page = user_data.get(call.from_user.id, 0)
    action = call.data.split("_")[1]

    if action == "incr":
        user_data[call.from_user.id] = first_page + 1
        await btn_get_news(call.message, first_page+1)
    elif action == "decr":
        user_data[call.from_user.id] = first_page - 1
        await btn_get_news(call.message, first_page-1)
    elif action == "finish":
        await call.message.edit_text(first_page)
    await call.answer()


@dp.message_handler(Text(equals=["✅ Підписатися/❌ Відписатися"]))
async def btn_subscribe(message: Message):
    try:
        async with db.connection.cursor() as cursor:
            await cursor.execute(f"SELECT news FROM users WHERE user_id = {message.from_user.id}")
            status = int(''.join(map(str, await cursor.fetchone())))
            if status == 0:
                await cursor.execute(f"UPDATE users SET news = 1 WHERE user_id = {message.from_user.id}")
                await message.answer("✅ Ви успішно підписалися!")
            else:
                await cursor.execute(f"UPDATE users SET news = 0 WHERE user_id = {message.from_user.id}")
                await message.answer("❌ Ви успішно відпідписалися!")
    except TypeError:
        await message.answer("❌ Схоже Ви не зареєстровані, виконайте команду /start та спробуйте ще!")
