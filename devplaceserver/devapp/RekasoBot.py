import telebot
import datetime

#794818784
bot = telebot.TeleBot('7492253580:AAGPpfoKY_Wz7VwVa0soifF2mUTR9A3mXVA')


def send_order(name, phone, tovar):
    bot.send_message("794818784", f'{name}\n{phone}\n{tovar}\n{datetime.datetime.now()}')


