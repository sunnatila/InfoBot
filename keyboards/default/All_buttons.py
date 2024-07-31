from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton

buttons_uz = ['🏢 Kompaniya haqida ma\'lumot', "⚒ Xizmatlar va mahsulotlar",
              "📰 Yangiliklar va yangilanishlar", "📈 Investorlar uchun bo'lim",
              "🧾 Hamkorlar uchun bo'lim", "📞 Aloqa ma'lumotlari", "❓ FAQ", "🌐 Tilni ozgartirish"]
buttons_ru = ['🏢 Информация о компании', "⚒ Услуги и продукты",
              "📰 Новости и обновления", "📈 Раздел для инвесторов",
              "🧾 Раздел для партнеров", "📞 Контактная информация", "❓ Часто задаваемые вопросы", "🌐 Изменить язык"]


async def create_menu_buttons(lang):

    if lang == 'uz':
        buttons_uzbek = ReplyKeyboardBuilder()
        for button_uz in buttons_uz:
            buttons_uzbek.add(KeyboardButton(text=f"{button_uz}"))
        return buttons_uzbek.adjust(2).as_markup(resize_keyboard=True)
    if lang == 'ru':
        buttons_russia = ReplyKeyboardBuilder()
        for button_ru in buttons_ru:
            buttons_russia.add(KeyboardButton(text=f"{button_ru}"))
        return buttons_russia.adjust(2).as_markup(resize_keyboard=True)


