from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton

lang = ReplyKeyboardBuilder(
    markup=[
        [
            KeyboardButton(text="O'zbek tili"),
            KeyboardButton(text="Русский язык"),
        ]
    ]
).adjust(2).as_markup(resize_keyboard=True)

