import logging
import math
from datetime import datetime

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.utils.exceptions import MessageNotModified, MessageTextIsEmpty

from keyboards.inline import search_scroll
from utils.elastcsearch.es import size_of_tenders, search_request
from keyboards.default import menu
from loader import dp


class SearchState(StatesGroup):
    request = State()


user_data = {}
request_handler = ""


@dp.message_handler(state=SearchState.request)
async def cmd_dialog(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
    global request_handler
    request_handler = user_message
    logging.info(request_handler)
    await message.answer(await get_tender_page(user_message, 0),
                         parse_mode='HTML', reply_markup=search_scroll,
                         disable_web_page_preview=True)
    await state.finish()
    await message.answer("Виберіть, будь ласка, зі списку", reply_markup=menu)


async def update_text(message: Message, new_value: int):
    tender_page = await get_tender_page(request_handler, new_value)
    try:
        await message.edit_text(tender_page, parse_mode='HTML',
                                reply_markup=search_scroll, disable_web_page_preview=True)
    except MessageTextIsEmpty:
        logging.info("News MessageTextIsEmpty")
    except MessageNotModified:
        logging.info("News MessageNotModified")


async def get_tender_page(user_message, page: int):
    """ Формує вивід однієї сторінки тендерів """
    try:
        logging.info("---------------------")
        logging.info(user_message)
        logging.info("---------------------")
        size_res = size_of_tenders(user_message)
        search_res = search_request(user_message, size_res)
        answer = ""

        if page == 0:
            first_elem = 0
            last_elem = 5
        elif 0 < page <= math.ceil((size_res / 5)):
            counter = page * 5
            first_elem = 0 + counter
            last_elem = 5 + counter
        else:
            return

        for i in range(first_elem, last_elem):
            tender = search_res["hits"]["hits"][i]
            link = "<a href = \"https://tender-online.com.ua/tender/view/" + str(tender["_id"]) + "\"> ➡️</a>"
            publishedDate = datetime.strptime(tender["_source"]["publishedDate"][0:10], '%Y-%m-%d').strftime('%d.%m.%Y')
            title = tender["_source"]["title"]
            amount = str(tender["_source"]["amount"])
            currency = tender["_source"]["currency"]
            answer += f"{i + 1}. {title}{link}\nОчікування пропозиції\n<i>{publishedDate}</i>\n{amount}{currency}\n\n"
        return answer
    except IndexError:
        return "Нічого не знайшов 😔"


@dp.callback_query_handler(Text(startswith="search_"))
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
