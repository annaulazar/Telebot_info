import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram.filters import CommandStart, Command

from config import config
from core.handlers.basic import get_start, get_photo, get_hello, get_location, get_inline
from core.handlers.contac import get_true_contact, get_fake_contact
from core.handlers.callback import select_macbook
from core.filters.iscontact import IsTrueContact
from core.utils.commands import set_commands
from core.utils.callbackdata import MacInfo


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(config.bot.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(config.bot.admin_id, text='Бот остановлен')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    bot = Bot(token=config.bot.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_inline, Command(commands='inline'))
    dp.callback_query.register(select_macbook, MacInfo.filter(F.model == 'pro'))
    dp.message.register(get_location, F.location)
    dp.message.register(get_hello, F.text.lower() == 'привет')
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
