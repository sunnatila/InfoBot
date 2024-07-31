from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from loader import db


class NewsCallbackData(CallbackData, prefix='news'):
    news_id: int
    level: int


async def create_news_callback_data(news_id: int, level: int):
    return NewsCallbackData(news_id=news_id, level=level).pack()


async def create_news_buttons(lang):
    CURRENT_LEVEL = 0
    news = await db.get_news_title(lang)
    if news:
        news_buttons = InlineKeyboardBuilder()
        for news_button in news:
            news_buttons.add(InlineKeyboardButton(
                text=f"{news_button[1]}",
                callback_data=await create_news_callback_data(news_button[0], CURRENT_LEVEL + 1)
            ))

        news_buttons.add(InlineKeyboardButton(
            text=f"{'⬅️ Oynani yopish' if lang == 'uz' else '⬅️ Закройте окно'}",
            callback_data=await create_news_callback_data(0, CURRENT_LEVEL - 1)
        ))
        return news_buttons.adjust(1).as_markup()
    else:
        return InlineKeyboardBuilder().add(InlineKeyboardButton(
            text=f"{'⬅️ Oynani yopish' if lang == 'uz' else '⬅️ Закройте окно'}",
            callback_data=await create_news_callback_data(0, CURRENT_LEVEL - 1)
        )).as_markup()


async def create_back_button(lang):
    CURRENT_LEVEL = 1
    return InlineKeyboardBuilder().add(InlineKeyboardButton(
        text=f"{'🔙 Orqaga' if lang == 'uz' else '🔙 Назад'}",
        callback_data=await create_news_callback_data(0, CURRENT_LEVEL - 1)
    )).as_markup()


async def send_news(lang, news_id):
    get_news_info = await db.get_news_info(lang, news_id)
    if lang == 'uz':
        news_info = f"Yangilik haqida ma'lumot: \n\n"
        news_info += f"{get_news_info[1]}\n"
        news_info += f"{get_news_info[2]}\n"
        news_image = f"{get_news_info[3]}\n"
    else:
        news_info = f"Информация о новости: \n\n"
        news_info += f"{get_news_info[1]}\n"
        news_info += f"{get_news_info[2]}\n"
        news_image = f"{get_news_info[3]}\n"
    return [news_info, news_image]
