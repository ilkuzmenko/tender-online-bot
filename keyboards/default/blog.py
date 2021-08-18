from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

blog = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙 Головне меню")
        ],
        [
            KeyboardButton(text="📩 Отримати новини"),
        ],
        [
            KeyboardButton(text="✅ Підписатися/❌ Відписатися")
        ],
    ],
    resize_keyboard=True
)