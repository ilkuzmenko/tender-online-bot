from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

share_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📲 Поділитися контактними даними", request_contact=True)
        ],
    ],
    resize_keyboard=True
)
