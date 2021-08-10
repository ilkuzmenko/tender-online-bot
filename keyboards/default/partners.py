from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

partners = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙 Головне меню")
        ],
        [
            KeyboardButton(text="⚖️ Правова підтримка")
        ],
        [
            KeyboardButton(text="📈 Аналітика ринку")
        ],
    ],
    resize_keyboard=True
)
