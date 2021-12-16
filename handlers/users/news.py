import math

from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from keyboards.inline import news_scroll
from loader import dp
from utils.mydb.comands import subscribe_user, get_news_sorted

user_data = {}


@dp.message_handler(Text(equals=["📩 Отримати новини"]))
async def get_news_btn(message: Message):
    """ Sends the user the first page of news """
    first_news_page = await get_news(page=0)
    if first_news_page:
        await message.answer(
            await get_news(page=0),
            parse_mode='HTML',
            reply_markup=news_scroll,
            disable_web_page_preview=True
        )


async def change_news(call: CallbackQuery, page=0):
    """ Changes exiting news page """
    news_page = await get_news(page=page)
    if news_page and call.message != news_page:
        await call.message.edit_text(
            news_page,
            parse_mode='HTML',
            reply_markup=news_scroll,
            disable_web_page_preview=True)
        return
    await call.answer(
        text="Думаю, там нічого нема 🧐",
        show_alert=True)
    user_data[call.from_user.id] = 0


@dp.callback_query_handler(Text(startswith="news_"))
async def callbacks_num(call: CallbackQuery):
    """ Implementation of message scrolling """
    first_page = user_data.get(call.from_user.id, 0)
    action = call.data.split("_")[1]
    if action == "incr":
        user_data[call.from_user.id] = first_page + 1
        await change_news(call, first_page+1)
    elif action == "decr":
        user_data[call.from_user.id] = first_page - 1
        await change_news(call, first_page-1)
    await call.answer()


@dp.message_handler(Text(equals=["✅ Підписатися/❌ Відписатися"]))
async def btn_subscribe(message: Message):
    """ Notifies the user of the subscription status """
    await message.answer(
        await subscribe_user(user_id=message.from_user.id)
    )


async def get_news(page: int):
    """ Формує вивід для однієї сторінки дописів """

    news_tuple = await get_news_sorted()

    if not news_tuple:
        return None

    out = '<b>📩 Новини:</b>\n\n'

    if page == 0:
        first_elem = 0
        last_elem = 5
    elif 0 < page <= math.ceil((len(news_tuple) / 5)):
        counter = page * 5
        first_elem = 0 + counter
        last_elem = 5 + counter
    else:
        return

    for i, news_dict in enumerate(news_tuple[first_elem:last_elem]):
        page_num = i + 1 + (page * 5)
        title = news_dict[1]
        date_post = str(news_dict[3])
        link = f"<a href = \"{news_dict[2]}\"> «детальніше»</a>"

        out += f"<b>{page_num}. {title}\n</b><i>{date_post}</i>\n{link}\n\n"

    return out
