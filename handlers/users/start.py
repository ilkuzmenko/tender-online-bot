import logging

from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from loader import dp, _
from keyboards.default import menu, share_contact
from utils.mydb.comands import add_user, subscription_status


@dp.message_handler(Command("start"))
async def phone(message: Message):
    if not bool(await subscription_status(user_id=message.from_user.id)):
        await message.answer(_(
            "Привіт, залишився один крок, "
            "поділіться Вашими контактними даними, "
            "щоб почати користуватися ботом."),
            reply_markup=share_contact
        )
    else:
        logging.info("User " + str(message.from_user.id) + " logged in bot.")
        await message.answer(_("Раді Вас бачити!"), reply_markup=menu)


@dp.message_handler(content_types=['contact'])
async def contact(message):
    if message.contact is not None:
        await add_user(
            message.from_user.id,
            int(message.contact.phone_number),
            message.contact.first_name,
            message.contact.last_name
        )
        logging.info("User " + str(message.from_user.id) + " signed in bot.")
        await message.answer(_("Оберіть, будь ласка, зі списку ⬇️"), reply_markup=menu)
