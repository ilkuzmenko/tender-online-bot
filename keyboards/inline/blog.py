from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

blog = InlineKeyboardMarkup()
blog.add(InlineKeyboardButton(text="⬅️", callback_data="num_decr"),
         InlineKeyboardButton(text="➡️", callback_data="num_incr"))
