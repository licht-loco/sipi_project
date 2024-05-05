from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
from database import get_schedule

API_TOKEN = ''
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Клавиатура с днями недели
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(types.KeyboardButton("Понедельник"),
             types.KeyboardButton("Вторник"),
             types.KeyboardButton("Среда"),
             types.KeyboardButton("Четверг"),
             types.KeyboardButton("Пятница"),
             types.KeyboardButton("Суббота"))

# Обработчик команды /schedule
@dp.message_handler(commands=['schedule'])
async def schedule_handler(message: types.Message):
    await message.answer("Выберите день недели:", reply_markup=keyboard)

# Обработчик нажатия на кнопку с днем недели
@dp.message_handler(lambda message: message.text in ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"])
async def get_schedule_handler(message: types.Message):
    day = message.text
    schedule = get_schedule(day)
    if schedule:
        response = "\n".join(f"{subject}: {time}" for subject, time in schedule)
    else:
        response = "Расписание пусто"
    await message.answer(response)

async def on_startup(dp):
    # Дополнительные действия при старте
    pass

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
