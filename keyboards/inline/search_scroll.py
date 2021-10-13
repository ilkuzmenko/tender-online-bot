from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

search_scroll = InlineKeyboardMarkup()
search_scroll.add(InlineKeyboardButton(text="⬅️", callback_data="search_decr"),
                  InlineKeyboardButton(text="➡️", callback_data="search_incr"))
