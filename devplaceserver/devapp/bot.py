import telebot
from .models import Manager

bot = telebot.TeleBot('6108543431:AAERHzKKCnfhPpU-zW29B-5D3zUFmsQzao0')

def send_message_lead(user):
    managers = Manager.objects.all()
    for i in managers:
        bot.send_message(i.chat_id, f'{user.name} \n{user.contact} \n{user.time} \n{user.comment}')

def send_lead(number):
    managers = Manager.objects.all()
    for i in managers:
        bot.send_message(i.chat_id, f'{number}')