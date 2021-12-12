from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, ContentTypes, ReplyKeyboardRemove
from utils.elastcsearch.es import get_tenders
from keyboards.default import menu
from loader import dp


class SearchState(StatesGroup):
    waiting_for_tender_region = State()
    waiting_for_tender_request = State()


@dp.message_handler(state=SearchState.waiting_for_tender_region, content_types=ContentTypes.TEXT)
async def region_step(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
    await message.answer("Напишіть пошуковий запит", reply_markup=ReplyKeyboardRemove())
    await SearchState.waiting_for_tender_request.set()


@dp.message_handler(state=SearchState.waiting_for_tender_request)
async def request_step(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['request'] = message.text

    tenders = await get_tenders(data['request'], region=data['region'])

    # print(info)
    if len(tenders) > 4096:
        index, start_index, div_blocks = 0, 0, 0
        for current_value, next_value in zip(tenders, tenders[1:]):
            index += 1
            if (current_value == next_value == '\n') and (div_blocks != 15):
                div_blocks += 1
            elif div_blocks == 15:
                # print(div_blocks, ' items ', [start_index, index])
                await message.answer(tenders[start_index:index], parse_mode='HTML', disable_web_page_preview=True)
                start_index = index
                div_blocks = 0
        # print(index, div_blocks)
    else:
        await message.answer(tenders, parse_mode='HTML', disable_web_page_preview=True)

    await state.finish()
    await message.answer("Оберіть зі списку", reply_markup=menu)



