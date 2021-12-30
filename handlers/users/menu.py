from loader import _

from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message

from handlers.users.search import SearchState
from keyboards.default import menu, faq, tariff, partners, blog, regions
from loader import dp


@dp.message_handler(Command("menu"))
async def menu_command(message: Message):
    await message.answer(_("Оберіть, будь ласка, зі списку ⬇️"), reply_markup=menu)


@dp.message_handler(Text(equals=[_("🔙 Головне меню")]))
async def back_to_menu(message: Message):
    await message.answer(_("Оберіть, будь ласка, зі списку ⬇️"), reply_markup=menu)


@dp.message_handler(Text(equals=[_("📎 Новини")]))
async def subscribe(message: Message):
    await message.answer(_("Оберіть, будь ласка, зі списку ⬇️"), reply_markup=blog)


@dp.message_handler(Text(equals=[_("🔎 Пошук")]))
async def search(message: Message):
    await message.answer("Оберіть область/регіон, зі списку ⬇️", reply_markup=regions)
    await SearchState.waiting_for_tender_region.set()


@dp.message_handler(Text(equals=[_("🆘 FAQ")]))
async def faq_menu(message: Message):
    await message.answer(_("Оберіть, будь ласка, зі списку ⬇️"), reply_markup=faq)


@dp.message_handler(Text(equals=[_("💰 Тарифи")]))
async def tariff_menu(message: Message):
    await message.answer(_("Оберіть, будь ласка, зі списку ⬇️"), reply_markup=tariff)


@dp.message_handler(Text(equals=[_("⭐️ Написати керівнику")]))
async def chef_help(message: Message):
    await message.answer(
        _("<b>⭐ Шановний клієнте!</b>\n"
          "Якщо Вам потрібно зв’язатись з керівником майданчика ТЕНДЕР-online, напишіть повідомлення @********\n"
          "Ми завжди вдячні за зворотній зв’язок."),
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[_("🔵 Про Prozorro")]))
async def prozorro_about(message: Message):
    await message.answer(
        _("<a href=\"https://prozorro.gov.ua/about\">🔵 Про Prozorro</a>\n\n"
          "⠀⠀⠀⠀<b>Prozorro</b> — електронна система публічних закупівель, де державні та комунальні"
          " замовники оголошують тендери на закупівлю товарів, робіт і послуг, а представники бізнесу"
          " змагаються на торгах за можливість стати постачальником держави.\n"
          "⠀⠀⠀⠀Сфера публічних закупівель регулюється Законом України «Про публічні закупівлі», "
          "а головним нормотворчим органом у цій сфері є Департамент сфери публічних закупівель, "
          "який входить до складу Міністерства розвитку економіки, торгівлі та сільського господарства України.\n"
          "⠀⠀⠀⠀З 1 квітня 2016 року система Prozorro є обов’язковою для центральних органів "
          "влади та монополістів, а з 1 серпня — для всіх інших державних замовників.\n"
          "⠀⠀⠀⠀На <b>Prozorro</b> неможливо зареєструватися, адже це центральна база даних, "
          "яка приймає інформацію від усіх майданчиків, і одночасно синхронізує її між собою. "
          "Реєстрація можлива лише на акредитованому майданчику, який належить до бізнесових структур. "
          "Таким чином відсікається монополія державного підприємства над даними у державних закупівлях.\n"
          "⠀⠀⠀⠀<b>ТЕНДЕР-online</b> - це акредитований майданчик системи закупівель <b>Prozorro</b>, "
          "який має всі 5 рівнів акредитації, а також перший онлайн магазин для державних "
          "замовників - <b>Prozorro Market</b>."),
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[_("🤝 Партнерські послуги")]))
async def partners_menu(message: Message):
    await message.answer(_("Оберіть, будь ласка, зі списку ⬇️"), reply_markup=partners)
