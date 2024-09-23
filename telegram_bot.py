from telebot import TeleBot, types
import sqlite3
from data_base import select_game_name, select_random_records

button = types.InlineKeyboardMarkup()
button.add(types.InlineKeyboardButton(text='привіт', callback_data='button1'))
button.add(types.InlineKeyboardButton(text='ти', callback_data='button2'))

markup2 = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Button 1')
itembtn2 = types.KeyboardButton('Button 2')
markup2.add(itembtn1, itembtn2)


def telegram_bot():
    token = "7125954288:AAHuEUOPeZ_Ug_LnagHH6DSJqKxwidl_cA8"
    bot = TeleBot(token)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message,
                     "Привіт! Я ігровий бот. Введіть /buy_game, щоб купити гру, /popular_games, щоб отримати список"
                     " популярних і гор за платформою.")

    @bot.message_handler(commands=['buy_game'])
    def add_game(message):
        bot.reply_to(message, "Введіть назву гри:")

        bot.register_next_step_handler(message, process_game_name)

    def process_game_name(message):
        game = select_game_name(message.text)
        if game:
            bot.reply_to(message, f"Бажаєте купити {message.text}? [Перейдіть на наш сайт](http://127.0.0.1:8000/b"
                                  f"uy_game/{message.text}).", parse_mode='Markdown')
        else:
            bot.reply_to(message,
                         f"Вибачте, але гри {message.text} немає в наявності. Ви також можете переглянути наш кат"
                         f"алог і вибрати іншу гру!")

    @bot.message_handler(commands=['popular_games'])
    def show_popular_games(message):
        games = select_random_records()
        if games:
            game_list = "\n".join([f"{i + 1}. {game['name']}" for i, game in enumerate(games)])
            bot.reply_to(message, f"Ось шість популярних ігор, які ви можете переглянути:\n\n{game_list}")
        else:
            bot.reply_to(message, "На жаль, не вдалося знайти жодної гри.")

    bot.remove_webhook()
    bot.polling()
