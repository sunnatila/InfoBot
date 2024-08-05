from aiogram import types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from aiogram.types import CallbackQuery

from keyboards.default import lang, create_menu_buttons
from keyboards.inline import create_back_button
from loader import dp, db

buttons_uz = ['🏢 Kompaniya haqida ma\'lumot', "⚒ Xizmatlar va mahsulotlar",
              "📰 Yangiliklar va yangilanishlar", "📈 Investorlar uchun bo'lim",
              "🧾 Hamkorlar uchun bo'lim", "📞 Aloqa ma'lumotlari", "❓ FAQ", "🌐 Tilni ozgartirish"]
buttons_ru = ['🏢 Информация о компании', "⚒ Услуги и продукты",
              "📰 Новости и обновления", "📈 Раздел для инвесторов",
              "🧾 Раздел для партнеров", "📞 Контактная информация", "❓ Часто задаваемые вопросы", "🌐 Изменить язык"]


@dp.message(lambda msg: msg.text in ["🏢 Kompaniya haqida ma'lumot", "🏢 Информация о компании"])
async def send_company_info(msg: types.Message, state: FSMContext):
    language = 'uz' if "🏢 Kompaniya haqida ma'lumot" in msg.text else 'ru'

    company_info = await db.get_company_info(language)
    if company_info:
        if language == 'uz':
            info = f"Kompaniya haqida malumot: \n\n"
            info += f"Umumiy ma'lumot: {company_info[0]}\n"
            info += f"Tarix: {company_info[1]}\n"
            info += f"Missiya: {company_info[2]}\n"
            info += f"Kompaniyaning qarashlari: {company_info[3]}\n"
            if company_info[4]:
                image = company_info[4]
                await msg.answer_photo(photo=image, caption=info)
            else:
                await msg.answer(info)
        else:
            info = f"Информация о компании: \n\n"
            info += f"Общая информация: {company_info[0]}\n"
            info += f"История: {company_info[1]}\n"
            info += f"Миссия: {company_info[2]}\n"
            info += f"Вид деятельности: {company_info[3]}\n"

            if company_info[4]:
                image = company_info[4]
                await msg.answer_photo(photo=image, caption=info)
            else:
                await msg.answer(info)
    else:
        TEXTS = {
            'uz': "Kompaniya haqida ma'lumot topilmadi",
            'ru': "Информация о компании не найдена"
        }
        await msg.answer(TEXTS[language])

