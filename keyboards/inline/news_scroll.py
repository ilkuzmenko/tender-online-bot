from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

news_scroll = InlineKeyboardMarkup()
news_scroll.add(
    InlineKeyboardButton(text="⬅️", callback_data="news_decr"),
    InlineKeyboardButton(text="➡️", callback_data="news_incr")
)
