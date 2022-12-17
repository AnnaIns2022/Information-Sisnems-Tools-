import telebot
import random
from telebot import types
f = open('design.txt', 'r', encoding='UTF-8')
design = f.read().split('\n')
f.close()
f = open('color.txt', 'r', encoding='UTF-8')
color  = f.read().split('\n')
f.close()
bot = telebot.TeleBot('5900011275:AAFNFjma242AVgzkTGXPY01wW76ysVEvFVU')
@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Дизайн")
        item2=types.KeyboardButton("Цвет")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \nДизайн - для выбора наличия дизайна\nЦвет - для выбора цвета',  reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Дизайн' :
            answer = random.choice(design)
    elif message.text.strip() == 'Цвет':
            answer = random.choice(color)
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True, interval=0)