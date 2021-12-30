from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import _

regions = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_("🔙 Головне меню"))
        ],
        [
            KeyboardButton(text=_("Вся Україна")),
        ],
        [
            KeyboardButton(text=_("м.Київ")),
        ],
        [
            KeyboardButton(text=_("Автономна Республіка Крим")),
        ],
        [
            KeyboardButton(text=_("Вінницька")),
        ],
        [
            KeyboardButton(text=_("Волинська")),
        ],
        [
            KeyboardButton(text=_("Дніпропетровська")),
        ],
        [
            KeyboardButton(text=_("Донецька")),
        ],
        [
            KeyboardButton(text=_("Житомирська")),
        ],
        [
            KeyboardButton(text=_("Закарпатська")),
        ],
        [
            KeyboardButton(text=_("Запорізька")),
        ],
        [
            KeyboardButton(text=_("Івано-Франківська")),
        ],
        [
            KeyboardButton(text=_("Київська")),
        ],
        [
            KeyboardButton(text=_("Кіровоградська")),
        ],
        [
            KeyboardButton(text=_("Луганська")),
        ],
        [
            KeyboardButton(text=_("Львівська")),
        ],
        [
            KeyboardButton(text=_("Миколаївська")),
        ],
        [
            KeyboardButton(text=_("Одеська")),
        ],
        [
            KeyboardButton(text=_("Полтавська")),
        ],
        [
            KeyboardButton(text=_("Рівненська")),
        ],
        [
            KeyboardButton(text=_("Сумська")),
        ],
        [
            KeyboardButton(text=_("Тернопільська")),
        ],
        [
            KeyboardButton(text=_("Харківська")),
        ],
        [
            KeyboardButton(text=_("Херсонська")),
        ],
        [
            KeyboardButton(text=_("Хмельницька")),
        ],
        [
            KeyboardButton(text=_("Черкаська")),
        ],
        [
            KeyboardButton(text=_("Чернівецька")),
        ],
        [
            KeyboardButton(text=_("Чернігівська")),
        ],
        [
            KeyboardButton(text=_("м. Севастополь")),
        ],
    ],
    resize_keyboard=True
)
