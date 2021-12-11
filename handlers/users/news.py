from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from keyboards.inline import news_scroll
from loader import dp, db
from utils.horizontal_scroll import scroll, update_page
from utils.mydb.comands import get_news_page

user_data = {}


@dp.message_handler(Text(equals=["📩 Отримати новини"]))
async def btn_get_news(message: Message):
    news_page = await get_news_page(0)
    await message.answer(news_page,
                         parse_mode='HTML',
                         reply_markup=news_scroll,
                         disable_web_page_preview=True)


@dp.callback_query_handler(Text(startswith="news_"))
async def callbacks_num(call: CallbackQuery):
    await scroll(call, user_data, _update_news_page)


async def _update_news_page(message: Message, new_value: int) -> None:
    news_page = await get_news_page(new_value)
    await update_page(message, news_page, news_scroll)


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
