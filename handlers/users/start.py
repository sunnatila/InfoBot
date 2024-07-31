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


@dp.message(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    user = await db.get_user_from_id(message.from_user.id)

    if user:
        language = user[0]
        TEXTS = {
            'uz': "Pastdagi kerakli tugmachani bo'sing:",
            'ru': "Нажмите соответствующую кнопку ниже:"
        }
        await message.answer(TEXTS[language], reply_markup=await create_menu_buttons(language))

    else:
        await message.answer(f"Assalomu alaykum! Botimizga hush kelibsiz. Tilni tanlang.\n"
                             f"Здравствуйте! Добро пожаловать в наш бот. Выберите язык", reply_markup=lang)
        await state.set_state("choose_lang")


@dp.message(StateFilter('choose_lang'))
async def send_buttons(msg: types.Message, state: FSMContext):
    if msg.text == "O'zbek tili":
        language = 'uz'
    else:
        language = 'ru'
    await db.add_tg_user(language, msg.from_user.id)
    TEXTS = {
        'uz': "Pastdagi kerakli tugmachani bo'sing:",
        'ru': "Нажмите соответствующую кнопку ниже:"
    }
    await msg.answer(TEXTS[language], reply_markup=await create_menu_buttons(language))
    await state.clear()


@dp.message(F.text == "🌐 Tilni ozgartirish")
async def update_lang(msg: types.Message, state: FSMContext):
    await msg.answer("Tilni tanlang: ", reply_markup=lang)
    await state.set_state('change_lang')


@dp.message(StateFilter('change_lang'))
async def change_lang(msg: types.Message, state: FSMContext):
    user_id = msg.from_user.id
    if msg.text == "O'zbek tili":
        language = 'uz'
    else:
        language = 'ru'
    await db.update_user(language, user_id)
    TEXTS = {
        'uz': "Pastdagi kerakli tugmachani bo'sing:",
        'ru': "Нажмите соответствующую кнопку ниже:"
    }
    await msg.answer(TEXTS[language], reply_markup=await create_menu_buttons(language))
    await state.clear()


@dp.message(F.text == "🌐 Изменить язык")
async def update_lang(msg: types.Message, state: FSMContext):
    await msg.answer("Выберите язык: ", reply_markup=lang)
    await state.set_state('change_lang')




