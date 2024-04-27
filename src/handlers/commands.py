import logging

from aiogram import Router
from aiogram import types
from aiogram.filters.command import Command

router = Router()


@router.message(Command("info"))
async def cmd_info(message: types.Message):
    logging.info("Received info command from user %s", message.from_user.id)
    user_info = f"Username: {message.from_user.username}, First Name: {message.from_user.first_name}, Last Name: {message.from_user.last_name}, ID: {message.from_user.id}"
    await message.answer(f"Here is your information:\n{user_info}")

