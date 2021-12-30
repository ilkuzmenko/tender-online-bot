from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import _

tariff = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_("🔙 Головне меню"))
        ],
        [
            KeyboardButton(text=_("🔵 Prozorro")),
            KeyboardButton(text=_("🟢 Prozorro Market"))
        ],
    ],
    resize_keyboard=True
)
