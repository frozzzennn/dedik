# -*- coding: utf-8 -*-

import telebot

token = '2046949694:AAHm26RUuyd2sHpeDJYuEP1vIDIbiWV1Nco'
bot = telebot.TeleBot(token) 
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Оформить заказ', 'Помощь')
    bot.send_message(message.chat.id, 'Привет! Ты попал в бота для оформления заказа на дедик.\nДля оформления заказа нажми на кнопку "Оформить заказ".\nТекущие расценки:\n1 ядро/1 ГБ ОЗУ - 65 рублей\n2 ядра/4 ГБ ОЗУ - 125 рублей\n2 ядра/8 ГБ ОЗУ - 200 рублей\n4 ядра/16 ГБ ОЗУ - 325 рублей\n Также есть и другие, цена договорная\nВ зависимости от ГЕО цена может увеличиваться\nЕсть вопросы? Нажми на кнопку "Помощь"', reply_markup=keyboard)

@bot.message_handler(content_types=['text']) 
def start_page(message):
    if message.text.lower() == "оформить заказ":
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard1.row('Назад')
        bot.send_message(message.chat.id, 'Какой вам нужен дедик?\nОтправьте конфигурации и расположение сервера.\nЕсли вы новичок, я могу установить вам нужную программу или другой браузер, об этом также напишите', reply_markup=keyboard1)
        bot.register_next_step_handler(message, order)
    elif message.text.lower() == "помощь":
        keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard3.row('Назад')
        bot.send_message(message.chat.id, "Напишите вопрос, он будет отправлен администратору и вам ответят как можно скорее", reply_markup=keyboard3)
        bot.register_next_step_handler(message, question)
    else:
        bot.send_message(message.chat.id, "Неизвестный запрос") 

def order(message):
    if message.text.lower() != "назад":
        dedik = message.text
        adminorder = "Новый заказ от пользователя @" + message.chat.username + "\n" + dedik
        bot.send_message('1883879405', adminorder) 
        keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard4.row('Назад')
        bot.send_message(message.chat.id, 'Ваш заказ направлен администратору, в скором времени с вами свяжемся для оплаты и выдачи товара', reply_markup=keyboard4)
        bot.register_next_step_handler(message, back)
def question(message): 
    if message.text.lower() != "назад":
        question = "Вопрос от пользователя @" + message.chat.username + "\n" + message.text.lower() 
        bot.send_message('1883879405', question) 
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard2.row('Назад')
        bot.send_message(message.chat.id, "Ваш вопрос отправлен администрации", reply_markup=keyboard2)
        bot.register_next_step_handler(message, back)
   elif message.text.lower() == "назад":
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Оформить заказ', 'Помощь')
        bot.send_message(message.chat.id, 'Привет! Ты попал в бота для оформления заказа на дедик.\nДля оформления заказа нажми на кнопку "Оформить заказ".\nТекущие расценки:\n1 ядро/1 ГБ ОЗУ - 65 рублей\n2 ядра/4 ГБ ОЗУ - 125 рублей\n2 ядра/8 ГБ ОЗУ - 200 рублей\n4 ядра/16 ГБ ОЗУ - 325 рублей\n Также есть и другие, цена договорная\nВ зависимости от ГЕО цена может увеличиваться\nЕсть вопросы? Нажми на кнопку "Помощь"', reply_markup=keyboard)

def back(message):
    if message.text.lower() == "назад":
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Оформить заказ', 'Помощь')
        bot.send_message(message.chat.id, 'Привет! Ты попал в бота для оформления заказа на дедик.\nДля оформления заказа нажми на кнопку "Оформить заказ".\nТекущие расценки:\n1 ядро/1 ГБ ОЗУ - 65 рублей\n2 ядра/4 ГБ ОЗУ - 125 рублей\n2 ядра/8 ГБ ОЗУ - 200 рублей\n4 ядра/16 ГБ ОЗУ - 325 рублей\n Также есть и другие, цена договорная\nВ зависимости от ГЕО цена может увеличиваться\nЕсть вопросы? Нажми на кнопку "Помощь"', reply_markup=keyboard)

bot.polling() 