import config
import telebot
import os
import time
from SQLighter import SQLighter
import random
import utils

morning = []
core = []
spine = []
legs = []


bot = telebot.TeleBot(config.token)


# @bot.message_handler(commands=["check"])
# def check_id(message):
#     for f_id in tf:
#         bot.send_document(message.chat.id, f_id)


def generate_markup():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = {"Ранок", "Загальні", "Спина", "Ноги"}
    markup.add(*[telebot.types.KeyboardButton(btn) for btn in buttons])
    return markup


@bot.message_handler(commands=["test"])
def rfind_file_ids(message):
    for file in os.listdir('gifs/'):
        if file.split('.')[-1] == 'gif':
            f = open('gifs/' + file, 'rb')
            msg = bot.send_document(message.chat.id, f, None)
            bot.send_message(message.chat.id, msg.document.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)

#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, "Доброго ранку!")
#


def morning_workout():
    db_worker = SQLighter(config.database_name)
    mw = db_worker.get_morning().fetchall()
    db_worker.close()
    morning.extend(mw)
    return morning


def core_workout():
    db_worker = SQLighter(config.database_name)
    mw = db_worker.get_core().fetchall()
    db_worker.close()
    core.extend(mw)
    return core


def send_msg(msg, file, markup):
    bot.send_message(msg.chat.id, file[1])
    bot.send_message(msg.chat.id, file[2])
    bot.send_document(msg.chat.id, file[0], reply_markup=markup)


def random_workout(message, markup):
    db_worker = SQLighter(config.database_name)
    row = db_worker.get_rand()
    if message.text == "":
        pass
    else:
        bot.send_message(message.chat.id, row[4])
        bot.send_message(message.chat.id, row[3])
        bot.send_document(message.chat.id, row[1], reply_markup=markup)  # 2 arguement = FILE_ID
    time.sleep(3)
    db_worker.close()


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    markup = generate_markup()
    if message.text == "Ранок":
        if not morning:
            morning_workout()
            file = morning.pop()
            send_msg(message, file, markup)
        else:
            file = morning.pop()
            send_msg(message, file, markup)
    elif message.text == "Загальні":
        if not core:
            core_workout()
            file = core.pop()
            send_msg(message, file, markup)
        else:
            file = core.pop()
            send_msg(message, file, markup)

    #     bot.send_message(message.chat.id, "Вибач, я тебе поки що не розумію", reply_markup=markup)


btns = {morning: "Ранок", core: "Загальні"}
#if btns.get(msg.text):
#    xxx

#
# def generate_markup(answear):
#     markup = types.ReplyKeyboardMarkup
#
# tf = {'CgADAgADOQADIOtJST9Yy5-yQNSkAg',
# 'CgADAgADOwADIOtJSbpzjNcvDAO_Ag',
# 'CgADAgADOAADIOtJSWQOzKjzQeCuAg',
# 'CgADAgADPQADIOtJScwbg0BiIBz7Ag'}


if __name__ == '__main__':
    bot.polling(none_stop=True)


query = 'Who knows?'
beatles = ['john', 'paul', 'george', 'ringo']
