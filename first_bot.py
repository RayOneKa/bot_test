import telebot
from telebot import types # кнопки
from string import Template
from random import randint
import requests
import urllib

bot = telebot.TeleBot("972288295:AAH666u2dez6FNSM6hhURbjVomoSTgKbBM8")

last_message = None

@bot.message_handler(regexp='стикер')
def send_welcome(message):    
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI3Sl55repCpzG_pSDzhPmPh9EF7lxUAAKrCQACeVziCVBwJLMZkNA7GAQ')

@bot.message_handler(regexp='космос')
def send_welcome(message):    

    url = 'https://apod.nasa.gov/apod/image/2003/BhShredder_NASA_1080.jpg'
    f = open('out.jpg','wb')
    f.write(urllib.request.urlopen(url).read())

    bot.send_photo(message.chat.id, open('out.jpg', 'rb'))    


# если /help, /start
@bot.message_handler(regexp='бот')
def send_welcome(message):
    messages = ['а? кто здесь?', 'Ну да, я - бот! И что?', 'На самом деле я папа botFather. Только тсс!', 'Zzz...', 'Всем привет!', 'Ну я так не играю...']
    ln = len(messages) - 1

    rnd = randint(0, ln)

    # удалить старую клавиатуру
    markup = types.ReplyKeyboardRemove(selective=False)

    bot.send_message(message.chat.id, messages[rnd])

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, "Что будем делать?\nУзнать курс валюты - /valute\nУзнать прогноз погоды - /weather\n", parse_mode="Markdown")

@bot.message_handler(commands=['valute'])
def send_start(message):
    bot.send_message(message.chat.id, "валюта...")    

@bot.message_handler(commands=['weather'])
def send_start(message):
    msg = bot.send_message(message.chat.id, "Введите, пожалуйста, город")    

    bot.register_next_step_handler(msg, city_choose)

def city_choose(message):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={message.text},ru&APPID=3c476f22a5b257b9d84b96dbf18ad854'

    response = requests.get(url).json()

    bot.send_message(message.chat.id, f"В городе {message.text} сейчас примерно {int(response['main']['temp'] - 273.15)} градусов")  


if __name__ == '__main__':
    bot.infinity_polling(none_stop=True)