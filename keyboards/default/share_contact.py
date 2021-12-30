from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import _

share_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_("📲 Поділитися контактними даними"), request_contact=True)
        ],
    ],
    resize_keyboard=True
)
