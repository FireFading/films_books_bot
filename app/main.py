import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from app.config import settings
from app.handlers.users import router as user_router


def setup_handlers(dp: Dispatcher) -> None:
    dp.include_router(user_router)


async def main() -> None:
    dp = Dispatcher()
    setup_handlers(dp=dp)
    bot = Bot(settings.token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    asyncio.run(main())
