from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import _

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_("🔎 Пошук")),
            KeyboardButton(text=_("📎 Новини"))
        ],
        [
            KeyboardButton(text=_("🆘 FAQ")),
            KeyboardButton(text=_("💰 Тарифи"))
        ],
        [
            KeyboardButton(text=_("⭐️ Написати керівнику")),
            KeyboardButton(text=_("🔵 Про Prozorro"))
        ],
        [
            KeyboardButton(text=_("🤝 Партнерські послуги"))
        ],
    ],
    resize_keyboard=True
)
