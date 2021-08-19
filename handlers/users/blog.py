import logging

from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from aiogram.utils.exceptions import MessageNotModified, MessageTextIsEmpty

from keyboards.inline import blog
from loader import dp, db
from utils.db.comands import get_blog_page, subscribe_user

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

user_data = {}


@dp.message_handler(Text(equals=["📩 Отримати новини"]))
async def btn_get_blog(message: Message):
    user_data[message.from_user.id] = 0
    blog_page = await get_blog_page(0)
    await message.answer(blog_page, parse_mode='HTML', reply_markup=blog)
    logging.info("btn_get_blog")


async def update_text(message: Message, new_value: int):
    blog_page = await get_blog_page(new_value)
    try:
        await message.edit_text(blog_page, parse_mode='HTML', reply_markup=blog)
    except MessageTextIsEmpty:
        logging.info("MessageTextIsEmpty")
    except MessageNotModified:
        logging.info("MessageNotModified")


@dp.callback_query_handler(Text(startswith="num_"))
async def callbacks_num(call: CallbackQuery):
    logging.info("pre callbacks")
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
    if not bool(await db.pool.fetchval('SELECT blog FROM users WHERE user_id = $1', message.from_user.id)):
        await subscribe_user(True, message.from_user.id)
        await message.answer("✅ Ви успішно підписалися!")
    else:
        await subscribe_user(False, message.from_user.id)
        await message.answer("❌ Ви успішно відпідписалися!")
