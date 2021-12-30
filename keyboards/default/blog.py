from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import _

blog = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_("🔙 Головне меню"))
        ],
        [
            KeyboardButton(text=_("📩 Отримати новини")),
        ],
        [
            KeyboardButton(text=_("✅ Підписатися/❌ Відписатися"))
        ],
    ],
    resize_keyboard=True
)
