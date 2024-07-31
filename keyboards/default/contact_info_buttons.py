from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder


async def create_contact_info_button(lang):
    if lang == 'uz':
        contact_buttons = ReplyKeyboardBuilder(
            markup=[
                [
                    KeyboardButton(text="🏢 Kompaniyaning manzili"),
                    KeyboardButton(text="📲 Kompaniyaning telefon raqamlari"),
                    KeyboardButton(text="📧 Kompaniyaning elektron manzili"),
                    KeyboardButton(text="🌐 Kompaniyaning ijtimoiy tarmoqlari"),
                    KeyboardButton(text="🔙 Qaytish"),
                ]
            ]
        )
    else:
        contact_buttons = ReplyKeyboardBuilder(
            markup=[
                [
                    KeyboardButton(text="🏢 Адрес компании"),
                    KeyboardButton(text="📲 Номера телефонов компании"),
                    KeyboardButton(text="📧 Электронная почта компании"),
                    KeyboardButton(text="🌐 Социальные сети компании"),
                    KeyboardButton(text="🔙 Назад"),
                ]
            ]
        )

    return contact_buttons.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=True)
