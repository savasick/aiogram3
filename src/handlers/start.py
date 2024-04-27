import logging

from aiogram import Router
from aiogram import types
from aiogram.filters.command import Command

from src.keyboards.main import build_main_keyboard

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    logging.info("Received start command from user %s", message.from_user.id)
    await message.answer("yolo?", reply_markup=build_main_keyboard())
