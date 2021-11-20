import logging

from aiogram.utils.exceptions import MessageTextIsEmpty, MessageNotModified


async def scroll(call, user_data, update_text):
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


async def update_page(message, page, reply_markup):
    try:
        await message.edit_text(page,
                                parse_mode='HTML',
                                reply_markup=reply_markup,
                                disable_web_page_preview=True)
    except MessageTextIsEmpty:
        logging.info("News MessageTextIsEmpty")
    except MessageNotModified:
        logging.info("News MessageNotModified")
