import logging
import os
import json
import requests
import pytz
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
COLLECTION_ID = os.getenv('COLLECTION_ID')
TOKEN = os.getenv('TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Создать обращение", callback_data='create_request')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Добро пожаловать! Нажмите кнопку, чтобы создать обращение.', reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == 'create_request':
        await query.message.reply_text('Пожалуйста, напишите ваше обращение.')
    else:
        logger.warning(f"Неизвестная кнопка: {query.data}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    user_name = update.message.from_user.full_name

    url = 'https://app.yonote.ru/api/documents.create'
    headers = {
        'Content-type': 'application/json'
    }
    timezone = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    title = f"Обращение от {user_name} | {current_time}"
    data = {
        "title": title,
        "text": user_message,        # Замените на текст обращения
        "collectionId": COLLECTION_ID,  # Замените реальным ID коллекции
        "parentDocumentId": "b66597a5-e093-4851-bbf6-de92a73ff04a",
        "token": TOKEN,            # Замените на реальный токен
        "publish": True
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        response_data = response.json()
        if "data" in response_data and "url" in response_data["data"]:
            share_url = response_data["data"]["url"]
            complete_url = f"https://panorama.yonote.ru/share/5f1fb236-1cd8-4df0-9f55-3ed6b391619b{share_url}"
            await update.message.reply_text(f'<a href="{complete_url}">Ваше обращение</a>', parse_mode='HTML')
        else:
            await update.message.reply_text("Ваше обращение успешно отправлено, но мы не смогли получить ссылку на него.")
        print("Успешно отправлено:", response_data)
    else:
        await update.message.reply_text("Произошла ошибка при отправке обращения. Пожалуйста, попробуйте еще раз.")
        print("Ошибка:", response.status_code, response.text)

def main() -> None:
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()