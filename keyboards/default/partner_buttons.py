from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder


async def create_partners_buttons(lang):
    if lang == 'uz':
        partners_buttons = ReplyKeyboardBuilder(
            markup=[
                [
                    KeyboardButton(text="📄 Hamkorlik imkoniyatlari"),
                    KeyboardButton(text="📝 Hamkorlik uchun ariza yuborish"),
                    KeyboardButton(text="🔙 Qaytish")
                ]
            ]
        )
    else:
        partners_buttons = ReplyKeyboardBuilder(
            markup=[
                [
                    KeyboardButton(text="📄 Преимущества партнерства"),
                    KeyboardButton(text="📝 Заявка на партнерство"),
                    KeyboardButton(text="🔙 Назад")
                ]
            ]
        )

    return partners_buttons.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=True)
