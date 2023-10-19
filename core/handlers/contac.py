from aiogram import Bot
from aiogram.types import Message


async def get_true_contact(message: Message, bot: Bot):
    await message.answer(f'{message.from_user.first_name} отправил свой контакт '
                         f'{message.contact.phone_number}')


async def get_fake_contact(message: Message, bot: Bot):
    await message.answer(f'{message.from_user.first_name} отправил чужой контакт')