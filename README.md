# Panorama_bot

Этот проект представляет собой Telegram-бота, который позволяет пользователям создавать обращения. Бот построен с использованием Python и библиотеки `python-telegram-bot`.

## Функциональные возможности

- Интерактивный интерфейс с кнопками.
- Пользователи могут отправлять текстовые обращения.
- Обращения публикуются и создаются на платформе Yonote.
- Генерация уникальной ссылки на каждое обращение.

## Технологии

- Python
- `python-telegram-bot`
- Docker
- Pytz (для обработки временных зон)

## Установка

Для установки и запуска бота выполните следующие шаги:

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/azonov/Panorama_bot.git
   cd Panorama_bot
   ```

2. Скопируйте пример `.env` файла и настройте переменные окружения:

   ```bash
   cp .env.example .env
   ```

   Откройте `.env` файл и добавьте ваши токены:
   ```env
   TELEGRAM_TOKEN=your_telegram_bot_token
   TOKEN=your_api_token
   ```

3. Настройте Docker (если вы еще не установили Docker, следуйте [официальным инструкциям](https://docs.docker.com/get-docker/)).

4. Постройте Docker образ:

   ```bash
   make build
   ```

5. Запустите контейнер:

   ```bash
   make run
   ```

## Использование

После запуска контейнера, вы можете открыть Telegram и написать вашему боту команду `/start`, чтобы начать использование. Вы сможете создать обращение, просто следуя инструкциям.

## Логирование

Логи вашего бота можно просмотреть с помощью команды:

```bash
make logs
```

## Остановка и удаление

Чтобы остановить и удалить контейнер, вы можете использовать:

```bash
make clean
```
