from aiogram import Bot
from aiogram.types import CallbackQuery

from core.utils.callbackdata import MacInfo

# async def select_macbook(call: CallbackQuery, bot: Bot):
#     _, model, size, chip, year = call.data.split('_')
#     answer = (f'{call.message.from_user.first_name}, ты выбрал Apple Macbook {model} '
#               f'с диагональю экрана {size} дюймов, на чипе {chip} {year} года')
#     await call.message.answer(answer)
#     await call.answer()


async def select_macbook(call: CallbackQuery, bot: Bot, callback_data: MacInfo):
    answer = (f'{call.message.from_user.first_name}, ты выбрал Apple Macbook {callback_data.model} с диагональю '
              f'экрана {callback_data.size} дюймов, на чипе {callback_data.chip} {callback_data.year} года')
    await call.message.answer(answer)
    await call.answer()

