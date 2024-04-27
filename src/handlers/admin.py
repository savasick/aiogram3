import logging

from aiogram import Router
from aiogram import types
from aiogram.filters.command import Command
from src.middlewares.admin import AdminMiddleware

router = Router()
router.message.middleware(AdminMiddleware())

@router.message(Command("admin"))
async def cmd_info(message: types.Message):
    logging.info("Received ADMIN command from user %s", message.from_user.id)
    user_info = f"ID: {message.from_user.id}"
    await message.answer(f"ADMIN is here \n{user_info}")

