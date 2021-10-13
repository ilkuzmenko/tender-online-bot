from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

blog_scroll = InlineKeyboardMarkup()
blog_scroll.add(InlineKeyboardButton(text="⬅️", callback_data="blog_decr"),
                InlineKeyboardButton(text="➡️", callback_data="blog_incr"))
