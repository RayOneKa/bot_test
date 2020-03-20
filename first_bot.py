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

    global last_message
    if last_message == None:
        last_message = rnd = 0
    else:
        rnd = last_message
        while rnd != last_message:
            rnd = randint(0, ln)

    bot.send_message(message.chat.id, messages[rnd])


if __name__ == '__main__':
    bot.infinity_polling(none_stop=True)