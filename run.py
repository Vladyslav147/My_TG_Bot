import asyncio
from aiogram import Bot, Dispatcher

from app.database.models import Register_main
from app.hendlers import router


async def main():
    await Register_main()
    bot = Bot(token='7369177778:AAHUqpzFiyHhwfVtIjVlIce1YkAj__HJPnQ')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
