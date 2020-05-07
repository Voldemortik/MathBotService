import config
import telebot
import method
 
from method import *
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    markup.row('Список функций', 'Инструкция')
   
    bot.send_message(message.chat.id, 'Привет ' + message.from_user.first_name + ', я математический бот', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def Buttons(message):
    if message.text == 'Список функций':
        bot.send_message(message.chat.id, 
        "sinh, coshtanh, arcsinh, arccosh, arctanh, log10, log1p, exp, expm1, sqrt, abs, conj, " +
        "real, imag, complex, cos, sin, tan, arcsin, arccos, arctan, log")

    elif message.text == 'Инструкция':
        bot.send_message(message.chat.id,
        'В этом боте Вы вписываете пример который нужно решить,Вам нужно полностью записать уровнение и отправить боту,' +
        'если Вы записали всё правильно бот сможет решить уравнение,но если вы ошиблись Вам выдаст ошибку')
    else:
        formulka = message.text
        kek =  str(eval(checkFunctions(formulka)))
        bot.send_message(message.chat.id, kek)
        
if __name__ == '__main__':
    bot.polling(none_stop=True)