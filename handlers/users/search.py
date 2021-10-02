from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message

from utils.elastcsearch.es import size_of_tenders, search_request
from keyboards.default import menu
from loader import dp


class SearchState(StatesGroup):
    request = State()


@dp.message_handler(state=SearchState.request)
async def cmd_dialog(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
    await message.answer(get_tender_page(user_message), parse_mode='HTML')
    await state.finish()
    await message.answer("Виберіть, будь ласка, зі списку", reply_markup=menu)


def get_tender_page(user_message):
    """ Формує вивід однієї сторінки тендерів """
    try:
        size_res = size_of_tenders(user_message)
        search_res = search_request(user_message, size_res)
        answer = ""

        for i in range(10):
            tender = search_res["hits"]["hits"][i]
            link = "<a href = \"https://tender-online.com.ua/tender/view/" + str(tender["_id"]) + "\"> ➡️</a>"
            publishedDate = datetime.strptime(tender["_source"]["publishedDate"][0:10], '%Y-%m-%d').strftime('%d.%m.%Y')
            title = tender["_source"]["title"]
            amount = str(tender["_source"]["amount"])
            currency = tender["_source"]["currency"]
            answer += f"{title}{link}\nОчікування пропозиції\n<i>{publishedDate}</i>\n{amount}{currency}\n\n"

        return answer

    except IndexError:
        return "Нічого не знайшов 😔"
