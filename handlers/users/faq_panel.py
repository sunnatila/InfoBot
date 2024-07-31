from aiogram import types, F
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.default import create_invest_button, create_contact_button, create_menu_buttons, create_partners_buttons, \
    create_contact_info_button
from keyboards.inline import create_back_button

from keyboards.inline.faq_buttons import FAQCallbackData, create_faq_buttons, create_back_button_for_faq
from loader import dp, db


@dp.message(lambda msg: msg.text in ["❓ FAQ", "❓ Часто задаваемые вопросы"])
async def faq_panel(msg: types.Message):
    lang = 'uz' if msg.text == "❓ FAQ" else 'ru'
    TEXTS = {
        'uz': "Kerakli savolingizni tanlang: ",
        'ru': "Выберите интересующее вас вопрос: "
    }
    await msg.answer(TEXTS[lang], reply_markup=await create_faq_buttons(lang))


@dp.callback_query(FAQCallbackData.filter())
async def handle_faq_callback(call: CallbackQuery, callback_data: FAQCallbackData):
    lang = (await db.get_user_from_id(call.from_user.id))[0]
    level = callback_data.level
    if level == 0:
        await show_faq_buttons(lang, call)
    elif level == -1:
        await show_menu_buttons(lang, call)
    elif level == 1:
        await show_faq_panel(lang, call, callback_data)


async def show_menu_buttons(lang, call):
    language = lang
    await call.message.delete()
    TEXTS = {
        'uz': "Asosiy menyuga qaytdingiz:",
        'ru': "Вы вернулись в главное меню: "
    }
    await call.message.answer(TEXTS[language], reply_markup=await create_menu_buttons(language))


async def show_faq_buttons(lang, call):
    language = lang
    await call.message.delete()
    TEXTS = {
        'uz': "Kerakli savolingizni tanlang: ",
        'ru': "Выберите интересующее вас вопрос: "
    }
    await call.message.answer(TEXTS[lang], reply_markup=await create_faq_buttons(lang))


async def show_faq_panel(lang, call, callback_data):
    language = lang
    question_id = callback_data.question_id

    get_question_info = await db.get_faq_answers(language, question_id)
    print(get_question_info)
    if get_question_info:
        TEXTS = {
            'uz': {
                'question_and_answer': f"Savol: {get_question_info[0]}\nJavob: {get_question_info[1]}",
            },
            'ru': {
                'question_and_answer': f"Вопрос: {get_question_info[0]}\nОтвет: {get_question_info[1]}",
            }
        }
        await call.message.delete()
        await call.message.answer(f"{TEXTS[language]['question_and_answer']}",
                                  reply_markup=await create_back_button_for_faq(lang))
    else:
        await call.message.delete()
        TEXTS = {
            'uz': "Bu savol mavjud emas!",
            'ru': "Этот вопрос уже был решен!"
        }
        await call.message.answer(TEXTS[language], reply_markup=await create_back_button_for_faq(lang))
