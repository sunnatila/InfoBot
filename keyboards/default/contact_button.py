from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder


async def create_contact_button(lang):
    if lang == 'uz':
        contact_button = ReplyKeyboardBuilder(
            markup=[
                [
                    KeyboardButton(text="📱 Kontaktni yuborish", request_contact=True),
                ]
            ]
        ).adjust(2).as_markup(resize_keyboard=True)
    else:
        contact_button = ReplyKeyboardBuilder(
            markup=[
                [
                    KeyboardButton(text="📱 Отправить контакт", request_contact=True),
                ]
            ]
        ).adjust(2).as_markup(resize_keyboard=True)
    return contact_button
