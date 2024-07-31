from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder


async def create_invest_button(lang):
    if lang == 'uz':
        invest_button = ReplyKeyboardBuilder(
            markup=[
                [
                    KeyboardButton(text="🏛 Moliyaviy ma'lumotlar"),
                    KeyboardButton(text="📃 Investorlik uchun ariza topshirish"),
                    KeyboardButton(text="🔙 Orqaga")
                ]
            ]
        ).adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=True)
    else:
        invest_button = ReplyKeyboardBuilder(
            markup=[
                [
                    KeyboardButton(text="🏛 Финансовая информация"),
                    KeyboardButton(text="📃 Заявка на инвестиции"),
                    KeyboardButton(text="🔙 Назад")
                ]
            ]
        ).adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=True)
    return invest_button
