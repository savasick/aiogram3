from aiogram import Dispatcher, BaseMiddleware
from src.db.base import get_database_session
from src.config.settings import config


class AdminMiddleware(BaseMiddleware):
    def __init__(self):
        self.admin_id = int(config.BOT_ADMIN.get_secret_value())

    async def __call__(self, handler, event, data):
        if event.from_user.id != self.admin_id:
            await event.answer(f'You are not authorized to perform this action. {self.admin_id}')
            return
        await handler(event, data)