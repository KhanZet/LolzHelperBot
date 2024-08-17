from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

API_TOKEN = "7241637234:AAF_7mpgjyQUIB6SzJ4GZ_jcgp2KqMJfM9A"

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()


async def on_startup():
    print("Bot is started")


if __name__ == "__main__":
    dp.startup.register(on_startup)
    dp.run_polling(bot)
