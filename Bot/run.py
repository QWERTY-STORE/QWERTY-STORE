import threading
import nest_asyncio
from flask import Flask
import bot
import asyncio
import logging


#*   Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

app = Flask(__name__)



@app.route('/')
def home():
    logger.info('Received request for /')
    return 'Bot is running!'

def run_bot():
    nest_asyncio.apply()  # Разрешить несколько циклов событий
    asyncio.run(bot.main())

if __name__ == '__main__':
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    app.run(host='0.0.0.0', port=5000)