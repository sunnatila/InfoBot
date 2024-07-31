from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


async def create_back_button(lang):
    if lang == 'uz':
        back_button = InlineKeyboardBuilder(
            markup=[
                [
                    InlineKeyboardButton(text="Orqaga qaytish", callback_data="back")
                ]
            ]
        ).adjust(2).as_markup()
    else:
        back_button = InlineKeyboardBuilder(
            markup=[
                [
                    InlineKeyboardButton(text="Возвращаться", callback_data="back")
                ]
            ]
        ).adjust(2).as_markup()
    return back_button
