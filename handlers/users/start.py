import logging

from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from loader import dp, db
from keyboards.default import menu, share_contact
from utils.mydb.comands import add_user


@dp.message_handler(Command("start"))
async def phone(message: Message):
    async with db.connection.cursor() as cursor:
        await cursor.execute(f"SELECT * FROM users WHERE user_id = {message.from_user.id}")
        if not bool(await cursor.fetchone()):
            await message.answer("Привіт {0.first_name}, залишився один крок, поділіться Вашими контактними даними, "
                                 "щоб почати користуватися ботом.".format(message.from_user),
                                 reply_markup=share_contact)
        else:
            logging.info("User " + str(message.from_user.id) + " logged in bot.")
            await message.answer("Раді Вас бачити!", reply_markup=menu)


@dp.message_handler(content_types=['contact'])
async def contact(message):
    if message.contact is not None:
        await add_user(message.from_user.id, int(message.contact.phone_number),
                       message.contact.first_name, message.contact.last_name)
        logging.info("User " + str(message.from_user.id) + " signed in bot.")
        await message.answer("Виберіть, будь ласка, зі списку", reply_markup=menu)
