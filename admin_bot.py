from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
from database import create_table, add_schedule

API_TOKEN = '7093253206:AAEm4rguSLwJ7hq-5gFhlpnS6QnDhuOlLts'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Обработчик команды /add_schedule
@dp.message_handler(commands=['add_schedule'])
async def add_schedule_handler(message: types.Message):
    try:
        _, day, subject, time = message.text.split()
        add_schedule(day, subject, time)
        await message.answer("Расписание успешно добавлено!")
    except ValueError:
        await message.answer("Используйте: /add_schedule <день недели> <предмет> <время>")

async def on_startup(dp):
    create_table()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
