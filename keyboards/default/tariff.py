from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tariff = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙 Головне меню")
        ],
        [
            KeyboardButton(text="🔵 Prozorro"),
            KeyboardButton(text="🟢 Prozorro Market")
        ],
    ],
    resize_keyboard=True
)
