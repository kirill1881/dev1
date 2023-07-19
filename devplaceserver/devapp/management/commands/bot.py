import telebot
from telebot import types

from django.core.management.base import BaseCommand
from threading import Thread

from devplaceserver.devapp.models import Manager

bot = telebot.TeleBot('6108543431:AAERHzKKCnfhPpU-zW29B-5D3zUFmsQzao0')

@bot.message_handler()
def start(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Регистрация")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Hi', reply_markup=markup)
    if message.text == 'Регистрация':
        m = Manager()
        m.chat_id(message.chat.id)
        m.username(message.from_user.username)
        m.name(message.from_user.first_name)
        m.save()
    bot.polling()



t = Thread(target=start)
t.setDaemon(True)
t.start()