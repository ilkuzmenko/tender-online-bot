from datetime import datetime
from typing import Optional

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, ContentTypes, ReplyKeyboardRemove
from utils.elastcsearch.es import search_request
from keyboards.default import menu
from loader import dp, _


class SearchState(StatesGroup):
    waiting_for_tender_region = State()
    waiting_for_tender_request = State()


@dp.message_handler(state=SearchState.waiting_for_tender_region, content_types=ContentTypes.TEXT)
async def region_step(message: Message, state: FSMContext):
    """ Меню вибору регіону """
    async with state.proxy() as data:
        data['region'] = message.text

    if data['region'] == _("🔙 Головне меню"):
        await state.finish()
        await message.answer(_("Оберіть, будь ласка, зі списку ⬇️"), reply_markup=menu)
        return

    await message.answer(_("Напишіть пошуковий запит"), reply_markup=ReplyKeyboardRemove())
    await SearchState.waiting_for_tender_request.set()


@dp.message_handler(state=SearchState.waiting_for_tender_request)
async def request_step(message: Message, state: FSMContext):
    """ Формування повідомлень відповіді за запитом: (регіон + ключове слово) """
    async with state.proxy() as data:
        data['request'] = message.text

    tenders = await get_tenders(user_message=data['request'], region=data['region'])

    if len(tenders) > 4096:
        index, start_index, div_blocks = 0, 0, 0
        for current_value, next_value in zip(tenders, tenders[1:]):
            index += 1
            if (current_value == next_value == '\n') and (div_blocks != 15):
                div_blocks += 1
            elif div_blocks == 15:
                await message.answer(tenders[start_index:index], parse_mode='HTML', disable_web_page_preview=True)
                start_index = index
                div_blocks = 0
    else:
        await message.answer(tenders, parse_mode='HTML', disable_web_page_preview=True)

    await state.finish()
    await message.answer(_("Оберіть, будь ласка, зі списку"), reply_markup=menu)


async def get_tenders(user_message, region) -> Optional[str]:
    """ Формує вивід однієї сторінки тендерів """

    search_res = search_request(user_message, region)

    if search_res["hits"]["total"] == 0:
        return _("Нічого не знайшов 😔")

    answer = ""
    for i in range(search_res["hits"]["total"]):

        tender = search_res["hits"]["hits"][i]
        title = tender["_source"]["title"]
        publishedDate = datetime.strptime(tender["_source"]["publishedDate"][0:10], '%Y-%m-%d').strftime('%d.%m.%Y')
        amount = str(tender["_source"]["amount"])
        currency = tender["_source"]["currency"]
        link = "<a href = \"https://tender-online.com.ua/tender/view/" + str(tender["_id"]) + "\">«детальніше»</a>"
        answer += f"<b>{i+1}. {title}"\
                  "</b>\nОчікування пропозиції\n"\
                  f"<i>{amount}</i> {currency}\n"\
                  f"<i>{publishedDate}</i>\n"\
                  f"{link}\n\n"
    return answer
