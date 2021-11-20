import logging

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from handlers.users.news import scroll
from keyboards.inline import search_scroll
from utils.elastcsearch.es import get_tender_page
from keyboards.default import menu
from loader import dp
from utils.horizontal_scroll import update_page


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
                         parse_mode='HTML',
                         reply_markup=search_scroll,
                         disable_web_page_preview=True)
    await state.finish()
    await message.answer("Оберіть зі списку", reply_markup=menu)


async def update_search_page(message: Message, new_value: int):
    search_page = await get_tender_page(request_handler, new_value)
    await update_page(message, search_page, search_scroll)


@dp.callback_query_handler(Text(startswith="search_"))
async def callbacks_num(call: CallbackQuery):
    await scroll(call, user_data, update_search_page)
