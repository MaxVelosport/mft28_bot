import os
import logging
import asyncpg
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()
TOKEN = os.getenv("TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

# Логирование
logging.basicConfig(level=logging.INFO)

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Подключение к базе данных
async def connect_db():
    return await asyncpg.create_pool(DATABASE_URL)

db = None

async def init_db():
    global db
    db = await connect_db()

# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("/training"))
    keyboard.add(KeyboardButton("/progress"))
    keyboard.add(KeyboardButton("/motivation"))
    keyboard.add(KeyboardButton("/nutrition"))
    await message.answer("Привет! Это бот MFT28. Выбери, что тебе нужно:", reply_markup=keyboard)

# Команда /training
@dp.message_handler(commands=['training'])
async def training_command(message: types.Message):
    await message.answer("Выбери тренировку:\n1. Грудь и трицепс\n2. Спина и бицепс\n3. Ноги и плечи")

# Команда /progress
@dp.message_handler(commands=['progress'])
async def progress_command(message: types.Message):
    await message.answer("Прогресс пока не фиксируется. Скоро добавим статистику!")

# Команда /motivation
@dp.message_handler(commands=['motivation'])
async def motivation_command(message: types.Message):
    await message.answer("Ты можешь больше, чем ты думаешь! Грег Плитт.")

# Команда /nutrition
@dp.message_handler(commands=['nutrition'])
async def nutrition_command(message: types.Message):
    await message.answer("Правильное питание – 80% успеха! Следуй плану.")

# Запуск бота
async def main():
    await init_db()
    executor.start_polling(dp)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())