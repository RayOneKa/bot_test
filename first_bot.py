import telebot
from telebot import types # кнопки
from string import Template
from random import randint

bot = telebot.TeleBot("972288295:AAH666u2dez6FNSM6hhURbjVomoSTgKbBM8")

last_message = None

# если /help, /start
@bot.message_handler(regexp='бот')
def send_welcome(message):
    messages = ['а? кто здесь?', 'Ну да, я - бот! И что?', 'На самом деле я папа botFather. Только тсс!', 'Zzz...', 'Всем привет!', 'Ну я так не играю...']
    ln = len(messages) - 1

    rnd = randint(0, ln)

    bot.send_message(message.chat.id, messages[rnd])

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, "Вот он - я! Самый лучший бот")


if __name__ == '__main__':
    bot.infinity_polling(none_stop=True)