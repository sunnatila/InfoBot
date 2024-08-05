from aiogram import types, F
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default import create_invest_button, create_contact_button, create_partners_buttons, create_menu_buttons
from keyboards.inline import create_back_button
from loader import dp, db, bot


@dp.message(lambda msg: msg.text in ["🧾 Hamkorlar uchun bo'lim", "🧾 Раздел для партнеров"])
async def send_partner_info(msg: types.Message, state: FSMContext):
    lang = 'uz' if msg.text == "🧾 Hamkorlar uchun bo'lim" else 'ru'
    TEXTS = {
        'uz': "Pastdagi kerakli tugmachani bo'sing:",
        'ru': "Нажмите соответствующую кнопку ниже:"
    }
    await msg.answer(TEXTS[lang], reply_markup=await create_partners_buttons(lang))


@dp.message(lambda msg: msg.text in ["🔙 Qaytish", "🔙 Назад"])
async def send_partner_info(msg: types.Message, state: FSMContext):
    lang = 'uz' if msg.text == "🔙 Qaytish" else 'ru'
    TEXTS = {
        'uz': "Asosiy menyuga qaytdingiz:",
        'ru': "Вы вернулись в главное меню: "
    }
    await msg.answer(TEXTS[lang], reply_markup=await create_menu_buttons(lang))


@dp.message(lambda msg: msg.text in ["📄 Hamkorlik imkoniyatlari", "📄 Преимущества партнерства"])
async def send_partner_info(msg: types.Message, state: FSMContext):
    lang = 'uz' if msg.text == "📄 Hamkorlik imkoniyatlari" else 'ru'
    get_partner_info = await db.get_partners_info(lang)
    if get_partner_info:
        TEXTS = {
            'uz': {
                'partner_info': f"Hamkorlik imkoniyatlari haqida ma'lumot: \n\n{get_partner_info[0]}\n"
                                f"{get_partner_info[1]}\n{get_partner_info[2]}\n{get_partner_info[3]}"
            },
            'ru': {
                'partner_info': f"Преимущества партнерства: \n\n{get_partner_info[0]}\n"
                                f"{get_partner_info[1]}\n{get_partner_info[2]}\n{get_partner_info[3]}\n"
            },
        }
        await msg.answer(TEXTS[lang])
    else:
        TEXTS = {
            'uz': "Hamkorlik imkoniyatlari haqida ma'lumotlar topilmadi",
            'ru': "Информация о преимуществах партнерства не найдена"
        }
        await msg.answer(TEXTS[lang])


@dp.message(lambda msg: msg.text in ["📝 Hamkorlik uchun ariza yuborish", "📝 Заявка на партнерство"])
async def send_partner_info(msg: types.Message, state: FSMContext):
    lang = 'uz' if msg.text == "📝 Hamkorlik uchun ariza yuborish" else 'ru'
    TEXTS = {
        'uz': "Ism-Familiyangizni kiriting:",
        'ru': "Введите свое имя и фамилию:"
    }
    await msg.answer(TEXTS[lang], reply_markup=ReplyKeyboardRemove())
    await state.update_data({'lang': lang})
    await state.set_state('get_partner_fullname')


@dp.message(StateFilter('get_partner_fullname'))
async def get_partner_fullname(msg: types.Message, state: FSMContext):
    lang = await state.get_data()
    await state.update_data(fullname=msg.text)
    TEXTS = {
        'uz': "Telefon raqamingizni pastki tugmacha orqali yuboring:",
        'ru': "Отправьте свой номер телефона, нажав кнопку ниже:"
    }
    await msg.answer(TEXTS[lang['lang']], reply_markup=await create_contact_button(lang['lang']))
    await state.set_state('get_partner_phone')


@dp.message(StateFilter('get_partner_phone'), lambda msg: not msg.contact)
async def get_partner_phone_error(msg: types.Message, state: FSMContext):
    lang = await state.get_data()
    TEXTS = {
        'uz': "‼️ Telefon raqamingizni pastki tugmacha orqali yuboring.",
        'ru': "‼️ Отправьте свой номер телефона, нажав кнопку ниже."
    }
    await msg.answer(TEXTS[lang['lang']], reply_markup=await create_contact_button(lang['lang']))
    await state.set_state('get_partner_phone')
    return


@dp.message(StateFilter('get_partner_phone'), F.contact)
async def get_partner_phone(msg: types.Message, state: FSMContext):
    lang = await state.get_data()
    await state.update_data(phone=msg.contact.phone_number)
    TEXTS = {
        'uz': "Batafsil ma'lumotingizni kiriting:",
        'ru': "Напишите подробную информацию:"
    }
    await msg.answer(TEXTS[lang['lang']], reply_markup=ReplyKeyboardRemove())
    await state.set_state('get_partner_advice')


@dp.message(StateFilter('get_partner_advice'))
async def get_partner_advice(msg: types.Message, state: FSMContext):
    lang = await state.get_data()
    user_info = await state.get_data()
    user_fullname = user_info['fullname']
    user_phone = user_info['phone']
    user_advice = msg.text
    await db.add_partner(user_fullname, user_phone, user_advice)
    if lang['lang'] == 'uz':
        user_information = f"📄 Hamkorlik uchun ariza!\n\n"
        user_information += f"👤 Hamkorning Ism-Familiyasi: {user_fullname}\n"
        user_information += f"📱 Hamkorning Telefon raqami: {user_phone}\n"
        user_information += f"📝 Hamkorlik uchun ba'tafsil ma'lumot: {user_advice}"
        for admin in ADMINS:
            await bot.send_message(admin, user_information)
    else:
        user_information = f"📄 Заявка на партнерство!\n\n"
        user_information += f"👤 Имя и фамилия партнера: {user_fullname}\n"
        user_information += f"📱 Номер телефона партнера: {user_phone}\n"
        user_information += f"📝 Дополнительная информация для сотрудничества: {user_advice}"
        for admin in ADMINS:
            await bot.send_message(admin, user_information)
    TEXTS = {
        'uz': "Arizangiz muvaffaqiyatli tarzda qabul qilindi.",
        'ru': "Ваша заявка была успешно подана."
    }
    await msg.answer(TEXTS[lang['lang']], reply_markup=await create_partners_buttons(lang['lang']))
    await state.clear()
