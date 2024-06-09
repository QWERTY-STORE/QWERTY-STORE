from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import logging



#*   Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)



#*   Замените этот токен на ваш новый токен от BotFather
TOKEN = '7471037984:AAFTTzXqPUi_wFcRXcTHerdAkk6IfvPbfQ0'



#*   Основное меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info('Received /start command')
    keyboard = [
        [InlineKeyboardButton("WebSite", web_app=WebAppInfo(url="https://qwerty-store.github.io/QWERTY-STORE-SITE/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Добро пожаловать в QWERTY STORE! Нажмите кнопку ниже, чтобы открыть сайт!', reply_markup=reply_markup)




#*   Обработка данных, полученных из Web App
async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info('Received data from web app')
    received_data = update.message.web_app_data.data
    await update.message.reply_text(f"Received data: {received_data}")



#*   Команда 'start'
async def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))

    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())