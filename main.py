import asyncio
import logging


from aiogram import Bot, Dispatcher
from config import settings
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from routers import router as main_router


async def main():

    dp = Dispatcher()
    dp.include_router(main_router)
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
