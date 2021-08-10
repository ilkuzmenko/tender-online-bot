from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📎 Підписатися"),
            KeyboardButton(text="🔎 Пошук")
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
