from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types

def build_main_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text=str("/info")))
    builder.add(types.KeyboardButton(text=str("/start")))
    return builder.as_markup(resize_keyboard=True)