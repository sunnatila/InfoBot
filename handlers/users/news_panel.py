from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default import create_menu_buttons
from keyboards.inline import create_back_button, create_news_buttons, send_news
from keyboards.inline.news_buttons import NewsCallbackData
from loader import dp, db

buttons_uz = ["📰 Yangiliklar va yangilanishlar"]
buttons_ru = ["📰 Новости и обновления"]


@dp.message(lambda msg: msg.text in ["📰 Yangiliklar va yangilanishlar", "📰 Новости и обновления"])
async def send_news_info(msg: types.Message):
    language = (await db.get_user_from_id(msg.from_user.id))[0]
    TEXTS = {
        'uz': "Ko'rmoqchi bo'lgan yangilikni tanlang:",
        'ru': "Выберите новости, которые хотите видеть:"
    }

    await msg.answer(TEXTS[language], reply_markup=await create_news_buttons(language))


@dp.callback_query(NewsCallbackData.filter())
async def handle_news_callback(call: CallbackQuery, callback_data: NewsCallbackData):
    language = (await db.get_user_from_id(call.from_user.id))[0]
    level = callback_data.level
    if level == 1:
        await show_news_panel(language, call, callback_data)
    elif level == 0:
        await show_news_buttons(language, call)
    elif level == -1:
        await show_menu_buttons(language, call)


async def show_news_panel(lang, call, callback_data):
    language = lang
    news_id = callback_data.news_id

    news_info, news_image = await send_news(language, news_id)
    await call.message.delete()

    await call.message.answer_photo(photo=news_image, caption=news_info, reply_markup=await create_back_button(language))


async def show_news_buttons(lang, call):
    language = lang
    await call.message.delete()
    TEXTS = {
        'uz': "Ko'rmoqchi bo'lgan yangilikni tanlang:",
        'ru': "Выберите новости, которые хотите видеть:"
    }

    await call.message.answer(TEXTS[language], reply_markup=await create_news_buttons(language))


async def show_menu_buttons(lang, call):
    language = lang
    await call.message.delete()
    TEXTS = {
        'uz': "Asosiy menyuga qaytdingiz:",
        'ru': "Вы вернулись в главное меню: "
    }
    await call.message.answer(TEXTS[language], reply_markup=await create_menu_buttons(language))
