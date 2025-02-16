import json
import os
import random
import asyncio
import schedule
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.utils import executor

# Загрузка конфигурации
CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

config = load_config()
TOKEN = config["TOKEN"]
CHAT_ID = config["CHAT_ID"]
INTERVAL = config["INTERVAL"]

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Директория с фото
IMAGE_DIR = "images"
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

async def send_random_image():
    """Отправляет случайное изображение в канал."""
    images = [f for f in os.listdir(IMAGE_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    if images:
        image_path = os.path.join(IMAGE_DIR, random.choice(images))
        with open(image_path, "rb") as photo:
            await bot.send_photo(chat_id=CHAT_ID, photo=InputFile(photo))
        print(f"Фото отправлено: {image_path}")
    else:
        print("Нет фото для отправки.")

def schedule_task():
    """Запускает планировщик задач."""
    schedule.every(INTERVAL).seconds.do(lambda: asyncio.run(send_random_image()))
    
    while True:
        schedule.run_pending()
        asyncio.run(asyncio.sleep(1))

async def start_scheduler():
    """Запускает отправку фото в фоновом режиме."""
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, schedule_task)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Бот запущен! Загружайте фото в папку 'images', и они будут отправляться каждые 2 часа.")

@dp.message_handler(commands=["set_interval"])
async def set_interval(message: types.Message):
    global INTERVAL
    try:
        new_interval = int(message.text.split()[1])
        if new_interval < 60:
            await message.reply("Минимальный интервал - 60 секунд.")
            return

        INTERVAL = new_interval
        config["INTERVAL"] = new_interval
        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file, indent=4)
        
        await message.reply(f"Интервал обновлён: {new_interval} секунд.")
    except (IndexError, ValueError):
        await message.reply("Используйте команду: /set_interval [секунды]")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_scheduler())
    executor.start_polling(dp, skip_updates=True)

