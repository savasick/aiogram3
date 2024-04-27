import asyncio
import logging

from aiogram import Bot, Dispatcher

from src.db.base import setup_database
from src.config.settings import config
from src.handlers import setup_message_routers

logging.basicConfig(level=logging.INFO)

async def main() -> None:
    bot = Bot(config.BOT_TOKEN.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()

    setup_database()

    message_routers = setup_message_routers()
    dp.include_routers(message_routers)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())