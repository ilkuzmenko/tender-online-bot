from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import _

partners = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_("🔙 Головне меню"))
        ],
        [
            KeyboardButton(text=_("⚖️ Правова підтримка"))
        ],
        [
            KeyboardButton(text=_("📈 Аналітика ринку"))
        ],
    ],
    resize_keyboard=True
)
