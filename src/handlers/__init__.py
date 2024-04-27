from aiogram import Router

def setup_message_routers() -> Router:
    from . import start, commands, admin

    router = Router()
    router.include_routers(start.router)
    router.include_routers(commands.router)
    router.include_routers(admin.router)

    return router