from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from loader import db


class FAQCallbackData(CallbackData, prefix='faq'):
    question_id: int
    level: int


async def create_faq_callback_data(question_id: int, level: int):
    return FAQCallbackData(question_id=question_id, level=level).pack()


async def create_faq_buttons(lang):
    CURRENT_LEVEL = 0
    faq = await db.get_faq_questions(lang)
    if faq:
        faq_buttons = InlineKeyboardBuilder()
        for faq_button in faq:
            faq_buttons.add(InlineKeyboardButton(
                text=f"{faq_button[1]}",
                callback_data=await create_faq_callback_data(faq_button[0], CURRENT_LEVEL + 1)
            ))

        faq_buttons.add(InlineKeyboardButton(
            text=f"{'⬅️ Oynani yopish' if lang == 'uz' else '⬅️ Закройте окно'}",
            callback_data=await create_faq_callback_data(0, CURRENT_LEVEL - 1)
        ))
        return faq_buttons.adjust(1).as_markup()
    else:
        return InlineKeyboardBuilder().add(InlineKeyboardButton(
            text=f"{'⬅️ Oynani yopish' if lang == 'uz' else '⬅️ Закройте окно'}",
            callback_data=await create_faq_callback_data(0, CURRENT_LEVEL - 1)
        )).as_markup()


async def create_back_button_for_faq(lang):
    CURRENT_LEVEL = 1
    return InlineKeyboardBuilder().add(InlineKeyboardButton(
        text=f"{'🔙 Orqaga' if lang == 'uz' else '🔙 Назад'}",
        callback_data=await create_faq_callback_data(0, CURRENT_LEVEL - 1)
    )).as_markup()