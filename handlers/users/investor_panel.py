from aiogram import types, F
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default import create_invest_button, create_contact_button, create_menu_buttons, create_partners_buttons
from keyboards.inline import create_back_button
from loader import dp, db, bot

buttons_uz = ["📈 Investorlar uchun bo'lim", "🏛 Moliyaviy ma'lumotlar"]
buttons_ru = ["📈 Раздел для инвесторов", "🏛 Финансовая информация"]


@dp.message(lambda c: c.text in ["📈 Investorlar uchun bo'lim", '📈 Раздел для инвесторов'])
async def send_invest_info(msg: types.Message, state: FSMContext):
    lang = 'uz' if msg.text == "📈 Investorlar uchun bo'lim" else 'ru'
    TEXTS = {
        'uz': "Pastdagi kerakli tugmachani bo'sing:",
        'ru': "Нажмите соответствующую кнопку ниже:"
    }
    await msg.answer(TEXTS[lang], reply_markup=await create_invest_button(lang))


@dp.message(lambda c: c.text in ["🔙 Orqaga", "🔙 Назад"])
async def send_invest_info(msg: types.Message, state: FSMContext):
    lang = 'uz' if msg.text == "🔙 Orqaga" else 'ru'
    TEXTS = {
        'uz': "Asosiy menyuga qaytdingiz:",
        'ru': "Вы вернулись в главное меню: "
    }
    await msg.answer(TEXTS[lang], reply_markup=await create_menu_buttons(lang))


@dp.message(lambda msg: msg.text in ["📃 Investorlik uchun ariza topshirish", "📃 Заявка на инвестиции"])
async def send_invest_questions(msg: types.Message, state: FSMContext):
    language = 'uz' if msg.text == "📃 Investorlik uchun ariza topshirish" else 'ru'
    await state.set_data({'lang': language})
    TEXTS = {
        'uz': "Ism-Familiyangizni kiriting:",
        'ru': "Введите свое имя и фамилию:"
    }
    await msg.answer(TEXTS[language], reply_markup=ReplyKeyboardRemove())
    await state.set_state('get_fullname')


@dp.message(StateFilter('get_fullname'))
async def get_fullname(msg: types.Message, state: FSMContext):
    language = await state.get_data()
    await state.update_data(fullname=msg.text)
    TEXTS = {
        'uz': "Telefon raqamingizni pastki tugmacha orqali yuboring:",
        'ru': "Отправьте свой номер телефона, нажав кнопку ниже:"
    }

    await msg.answer(TEXTS[language['lang']], reply_markup=await create_contact_button(language['lang']))

    await state.set_state('get_phone')


@dp.message(StateFilter('get_phone'), lambda msg: not msg.contact)
async def get_phone_error(msg: types.Message, state: FSMContext):
    language = await state.get_data()
    TEXTS = {
        'uz': "‼️ Telefon raqamingizni pastki tugmacha orqali yuboring:",
        'ru': "‼️ Отправьте свой номер телефона, нажав кнопку ниже:"
    }
    await msg.answer(TEXTS[language['lang']], reply_markup=await create_contact_button(language['lang']))
    await state.set_state('get_phone')
    return


@dp.message(StateFilter('get_phone'), F.contact)
async def get_phone(msg: types.Message, state: FSMContext):
    language = await state.get_data()
    await state.update_data(phone=msg.contact.phone_number)
    TEXTS = {
        'uz': "Batafsil ma'lumotingizni kiriting:",
        'ru': "Напишите подробную информацию:"
    }
    await msg.answer(TEXTS[language['lang']], reply_markup=ReplyKeyboardRemove())
    await state.set_state('get_advice')


@dp.message(StateFilter('get_advice'))
async def get_advice(msg: types.Message, state: FSMContext):
    language = await state.get_data()
    user_info = await state.get_data()
    user_fullname = user_info['fullname']
    user_phone = user_info['phone']
    user_advice = msg.text
    await db.add_invest_user(user_fullname, user_phone, user_advice)
    if language['lang'] == 'uz':
        user_information = f"📃 Investorlik uchun ariza!\n\n"
        user_information += f"👤 Investorning Ism-Familiyasi: {user_fullname}\n"
        user_information += f"📞 Investorning telefon raqami: {user_phone}\n\n"
        user_information += f"📝 Investor bo'lish uchun ba'tafsil ma'lumot: {user_advice}\n"
        for admin in ADMINS:
            await bot.send_message(admin, user_information)
    else:
        user_information = f"📃 Заявка на инвестиции!\n\n"
        user_information += f"👤 Имя и фамилия инвестора: {user_fullname}\n"
        user_information += f"📞 Номер телефона инвестора: {user_phone}\n\n"
        user_information += f"📝 Дополнительная информация, чтобы стать инвестором: {user_advice}\n"
        for admin in ADMINS:
            await bot.send_message(admin, user_information)

    TEXTS = {
        'uz': 'Sizning arizangiz muvaffaqiyatli tarzda qabul qilindi.',
        'ru': 'Ваша заявка была успешно подана.'
    }
    await msg.answer(TEXTS[language['lang']], reply_markup=await create_partners_buttons(language['lang']))
    await state.clear()

# investor application
# ----------------------------------------------------------------------------------------------------------------------
# investor information for investor application


@dp.message(lambda msg: msg.text in ["🏛 Moliyaviy ma'lumotlar", "🏛 Финансовая информация"])
async def send_invest_info(msg: types.Message, state: FSMContext):
    lang = 'uz' if msg.text == "🏛 Moliyaviy ma'lumotlar" else 'ru'
    invest_info = await db.get_invest_info(lang)
    if invest_info:
        TEXTS = {
            'uz': {
                f"invest_info": f"🏛 Moliyaviy ma'lumotlar: \n\n{invest_info[0]}\n{invest_info[1]}"
                                f"\n{invest_info[2]}\n{invest_info[3]}",
                "invest_image": f"{invest_info[4]}"
            },
            'ru': {
                f"invest_info": f"🏛 Финансовая информация: \n\n{invest_info[0]}\n{invest_info[1]}"
                                f"\n{invest_info[2]}\n{invest_info[3]}",
                "invest_image": f"{invest_info[4]}"
            }
        }
        await msg.answer_photo(photo=TEXTS[lang]['invest_image'], caption=TEXTS[lang]['invest_info'])
    else:
        TEXTS = {
            'uz': "Moliyaviy ma'lumotlar topilmadi",
            'ru': "Финансовая информация не найдена"
        }
        await msg.answer(TEXTS[lang])
