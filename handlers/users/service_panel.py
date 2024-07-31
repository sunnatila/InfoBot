from aiogram import types

from loader import dp, db


@dp.message(lambda msg: msg.text in ["⚒ Xizmatlar va mahsulotlar", "⚒ Услуги и продукты"])
async def send_service_panel(msg: types.Message):
    language = 'uz' if "⚒ Xizmatlar va mahsulotlar" in msg.text else 'ru'
    get_service_info = await db.get_service_info(language)
    if get_service_info:
        TEXTS = {
            'uz': {
                'service_info': f"Xizmatlar haqida ma'lumot: \n\n{get_service_info[0]}\n\n"
                                f"Mahsulotlar haqida ma'lumot: \n{get_service_info[1]}",
            },
            'ru': {
                'service_info': f"Информация о услугах: \n\n{get_service_info[0]}\n\n"
                                f"Информация о продуктах: \n\n{get_service_info[1]}",
            }
        }

        await msg.answer(TEXTS[language]['service_info'])
    else:
        TEXTS = {
            'uz': "Xizmatlar va mahsulotlar haqida ma'lumotlar topilmadi",
            'ru': "Информация о продуктах и услугах не найдена"
        }
        await msg.answer(TEXTS[language])

