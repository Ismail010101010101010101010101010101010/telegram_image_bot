

Этот бот автоматически публикует загруженные в него изображения в Telegram-канале через заданный интервал времени.

##
- Автоматическая публикация изображений в Telegram-канале каждые 2 часа (по умолчанию).
- Возможность изменения интервала отправки изображений.

## 

### 

```bash
git clone <URL_вашего_репозитория>
cd telegram_image_bot
```

### 

```bash
python3 -m venv venv
source venv/bin/activate  # Для Linux и macOS
venv\Scripts\activate    # Для Windows
```

### 

```bash
pip install -r requirements.txt
```

###

Создайте файл `config.json` в корневой папке проекта со следующим содержимым:

```json
{
  "TOKEN": "YOUR_TELEGRAM_BOT_TOKEN",
  "CHAT_ID": "YOUR_TELEGRAM_CHAT_ID",
  "INTERVAL": 7200
}
```

- `TOKEN` — токен вашего бота (получите у @BotFather).
- `CHAT_ID` — ID вашего канала (получите у @userinfobot или другим способом).
- `INTERVAL` — интервал между отправками изображений в секундах (по умолчанию 7200 секунд = 2 часа).

### 

Создайте папку `images` в корне проекта и поместите в неё изображения, которые бот будет отправлять.

```bash
mkdir images
```

### 

```bash
python3 bot.py
```

✅ Бот начнёт отправлять изображения из папки `images` в канал с заданным интервалом.

## 

Чтобы бот работал 24/7:
- Используйте VPS (например, DigitalOcean, Linode или Hetzner).
- Бесплатные решения: Heroku, Railway или Render.

## 

- Остановить бота: `Ctrl + C`
- Выйти из виртуального окружения: `deactivate`


