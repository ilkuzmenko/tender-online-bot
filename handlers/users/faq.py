from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from loader import dp
from data.text_const import btnFAQ1_text, btnFAQ2_text, btnFAQ3_text, btnFAQ4_text, btnFAQ5_text, \
    btnFAQ6_text, btnFAQ7_text, btnFAQ8_text, btnFAQ9_text, btnFAQ10_text, \
    btnFAQ11_text, btnFAQ12_text, btnFAQ13_text, btnFAQ14_text, btnFAQ15_text, \
    btnFAQ16_text, btnFAQ17_text, btnFAQ18_text, btnFAQ19_text, btnFAQ20_text, \
    btnFAQ21_text, btnFAQ22_text, btnFAQ23_text, btnFAQ24_text, btnFAQ25_text, btnFAQ26_text


@dp.message_handler(Text(equals=["Чим відрізняються Допорогові/Спрощені закупівлі від Відкритих торгів?"]))
async def btn_faq1(message: Message):
    await message.answer(btnFAQ1_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Чим відрізняються «Допорогові закупівлі» та «Звіт про укладені договори»?"]))
async def btn_faq2(message: Message):
    await message.answer(btnFAQ2_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Як ідентифікуватися в системі?"]))
async def btn_faq3(message: Message):
    await message.answer(btnFAQ3_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Як поповнити рахунок (баланс компанії)?"]))
async def btn_faq4(message: Message):
    await message.answer(btnFAQ4_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Чому платна участь для постачальників?"]))
async def btn_faq5(message: Message):
    await message.answer(btnFAQ5_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Чи може від однієї організації бути зареєстровано декілька осіб?"]))
async def btn_faq6(message: Message):
    await message.answer(btnFAQ6_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Чи маємо ми можливість навчитися оголошувати закупівлю чи брати участь у закупівлі в "
                                "тестовому режимі?"]))
async def btn_faq7(message: Message):
    await message.answer(btnFAQ7_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Де можна знайти нормативні документи, які регулюють сферу публічних закупівель?"]))
async def btn_faq8(message: Message):
    await message.answer(btnFAQ8_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Як знайти оголошення про закупівлю на вашому майданчику?"]))
async def btn_faq9(message: Message):
    await message.answer(btnFAQ9_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Який мінімальний крок пониження ціни, як його вирахувати та хто його визначає?"]))
async def btn_faq10(message: Message):
    await message.answer(btnFAQ10_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Що таке КЕП (Кваліфікований електронний підпис)?"]))
async def btn_faq11(message: Message):
    await message.answer(btnFAQ11_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Чи є обов\'язковим використання КЕП для державних замовників та постачальників?"]))
async def btn_faq12(message: Message):
    await message.answer(btnFAQ12_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Як опублікувати оголошення?"]))
async def btn_faq13(message: Message):
    await message.answer(btnFAQ13_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Якого формату має бути прикріплена тендерна документація, а також пропозиції "
                                "учасників?"]))
async def btn_faq14(message: Message):
    await message.answer(btnFAQ_text14, parse_mode='HTML')


@dp.message_handler(Text(equals=["Чи може замовник вносити зміни в оголошення та документацію? Як правильно йому це "
                                "зробити?"]))
async def btn_faq15(message: Message):
    await message.answer(btnFAQ15_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Як подати тендерну пропозицію на участь у закупівлі?"]))
async def btn_faq16(message: Message):
    await message.answer(btnFAQ16_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Чи може учасник редагувати/видаляти свою тендерну пропозицію?"]))
async def btn_faq17(message: Message):
    await message.answer(btnFAQ17_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Чи може учасник звернутися до Замовника із запитинням?"]))
async def btn_faq18(message: Message):
    await message.answer(btnFAQ18_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Як замовнику розмістити відповідь на поставлене питання?"]))
async def btn_faq19(message: Message):
    await message.answer(btnFAQ19_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Якщо у закупівлі прийняв участь лише 1 постачальник, чи буде проводитися тендер?"]))
async def btn_faq20(message: Message):
    await message.answer(btnFAQ20_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Як Замовник може відмінити закупівлю або визнати її такою, що не відбулася?"]))
async def btn_faq21(message: Message):
    await message.answer(btnFAQ21_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Як Учасника закупівлі визначити переможцем або дискваліфікувати його?"]))
async def btn_faq22(message: Message):
    await message.answer(btnFAQ22_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Що робити в тому випадку, якщо обраний Переможець відмовляється від подальшої "
                                "співпраці?"]))
async def btn_faq23(message: Message):
    await message.answer(btnFAQ23_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Які подальші дії замовника після того, як він визнає переможця?"]))
async def btn_faq24(message: Message):
    await message.answer(btnFAQ24_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Що робити, якщо замовник отримав Вимогу про усунення порушення від одного з "
                                "учасників на етапі кваліфікації?"]))
async def btn_faq25(message: Message):
    await message.answer(btnFAQ25_text, parse_mode='HTML')


@dp.message_handler(Text(equals=["Чи може Учасник оскаржити рішення Замовника? Які тарифи на оскарження процедури "
                                "закупівлі?"]))
async def btn_faq26(message: Message):
    await message.answer(btnFAQ26_text, parse_mode='HTML')
