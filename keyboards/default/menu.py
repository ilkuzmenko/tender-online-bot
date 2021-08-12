from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔎 Пошук"),
            KeyboardButton(text="📎 Блог")
        ],
        [
            KeyboardButton(text="🆘 FAQ"),
            KeyboardButton(text="💰 Тарифи")
        ],
        [
            KeyboardButton(text="⭐️ Написати керівнику"),
            KeyboardButton(text="🔵 Про Prozorro")
        ],
        [
            KeyboardButton(text="🤝 Партнерські послуги")
        ],
    ],
    resize_keyboard=True
)
