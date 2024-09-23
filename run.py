from routes import *
import threading
from telegram_bot import telegram_bot

if __name__ == '__main__':
    threading.Thread(target=telegram_bot).start()
    app.run(port=8000, debug=True)
