import telebot
import os

# Берём токен из переменных среды (Railway)
TOKEN = os.getenv("TOKEN")

# Создаём бота
bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для мониторинга состояния ребёнка!")

# Обработчик любых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я пока умею только отвечать :)")

# Запуск бота
bot.polling()