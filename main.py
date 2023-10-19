import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram.filters import CommandStart, Command

from config import config
from core.handlers.basic import get_start, get_photo


async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    bot = Bot(token=config.bot.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_photo, F.photo)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
