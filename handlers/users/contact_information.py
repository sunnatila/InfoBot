from aiogram import types
from keyboards.default import create_menu_buttons, create_contact_info_button
from loader import dp, db


@dp.message(lambda msg: msg.text in ["📞 Aloqa ma'lumotlari", "📞 Контактная информация"])
async def send_contact_info(msg: types.Message):
    lang = 'uz' if msg.text == "📞 Aloqa ma'lumotlari" else 'ru'
    TEXTS = {
        'uz': "Pastdagi kerakli tugmachani bo'sing:",
        'ru': "Нажмите соответствующую кнопку ниже:"
    }
    await msg.answer(TEXTS[lang], reply_markup=await create_contact_info_button(lang))


@dp.message(lambda msg: msg.text in ["🏢 Kompaniyaning manzili", "🏢 Адрес компании"])
async def send_company_location(msg: types.Message):
    lang = 'uz' if msg.text == "🏢 Kompaniyaning manzili" else 'ru'
    company_address = await db.get_company_location(lang)
    if company_address:
        TEXTS = {
            'uz': f"Kompaniyaning manzili: {company_address[0]}",
            'ru': f"Адрес компании: {company_address[0]}"
        }
        await msg.answer(TEXTS[lang])
    else:
        TEXTS = {
            'uz': "Kompaniyaning manzili topilmadi",
            'ru': "Адрес компании не найден"
        }
        await msg.answer(TEXTS[lang])


@dp.message(lambda msg: msg.text in ["📲 Kompaniyaning telefon raqamlari", "📲 Номера телефонов компании"])
async def send_company_location(msg: types.Message):
    lang = 'uz' if msg.text == "📲 Kompaniyaning telefon raqamlari" else 'ru'
    company_contacts = await db.get_company_contact(lang)
    if company_contacts:
        TEXTS = {
            'uz': f"Kompaniyaning telefon raqamlari: {company_contacts[0]}",
            'ru': f"Номера телефонов компании: {company_contacts[0]}"
        }
        await msg.answer(TEXTS[lang])
    else:
        TEXTS = {
            'uz': "Kompaniyaning telefon raqamlari topilmadi",
            'ru': "Номера телефонов компании не найдены"
        }
        await msg.answer(TEXTS[lang])


@dp.message(lambda msg: msg.text in ["📧 Kompaniyaning elektron manzili", "📧 Электронная почта компании"])
async def send_company_location(msg: types.Message):
    lang = 'uz' if msg.text == "📧 Kompaniyaning elektron manzili" else 'ru'
    company_email = await db.get_company_email(lang)
    if company_email:
        TEXTS = {
            'uz': f"Kompaniyaning elektron manzili: {company_email[0]}",
            'ru': f"Электронная почта компании: {company_email[0]}"
        }
        await msg.answer(TEXTS[lang])
    else:
        TEXTS = {
            'uz': "Kompaniyaning elektron manzili topilmadi",
            'ru': "Электронная почта компании не найдена"
        }
        await msg.answer(TEXTS[lang])


@dp.message(lambda msg: msg.text in ["🌐 Kompaniyaning ijtimoiy tarmoqlari", "🌐 Социальные сети компании"])
async def send_company_location(msg: types.Message):
    lang = 'uz' if msg.text == "🌐 Kompaniyaning ijtimoiy tarmoqlari" else 'ru'
    company_social_networks = await db.get_company_social_networks(lang)
    if company_social_networks:
        TEXTS = {
            'uz': f"Kompaniyaning ijtimoiy tarmoqlari: {company_social_networks[0]}",
            'ru': f"Социальные сети компании: {company_social_networks[0]}"
        }
        await msg.answer(TEXTS[lang])
    else:
        TEXTS = {
            'uz': "Kompaniyaning ijtimoiy tarmoqlari topilmadi",
            'ru': "Социальные сети компании не найдены"
        }
        await msg.answer(TEXTS[lang])


@dp.message(lambda msg: msg.text in ["🔙 Qaytish", "🔙 Назад"])
async def send_contact_info(msg: types.Message):
    lang = 'uz' if msg.text == "🔙 Qaytish" else 'ru'
    TEXTS = {
        'uz': "Asosiy menyuga qaytdingiz:",
        'ru': "Вы вернулись в главное меню: "
    }
    await msg.answer(TEXTS[lang], reply_markup=await create_menu_buttons(lang))

