from aiogram import Bot
from aiogram.types import Message
from datetime import datetime


async def get_start(message: Message, bot: Bot):
    # await bot.send_message(message.from_user.id, f'<b>Привет, {message.from_user.first_name}</b>')
    await message.answer(f'<b>Привет {message.from_user.first_name}. Что интересует?</b>')
    # await message.reply(f'<tg-spoiler>Привет {message.from_user.first_name}</tg-spoiler>')


async def get_photo(message: Message, bot: Bot):
    print(message.photo[0].file_id)
    await message.answer(f'Отлично, {message.from_user.first_name} отправил картинку, я сохранил ее себе')
    file = await bot.get_file(file_id=message.photo[-1].file_id, request_timeout=1)

    await bot.download_file(file.file_path,
        f"downloaded_files/image_{message.from_user.id}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg")


async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе {message.from_user.first_name} привет')



