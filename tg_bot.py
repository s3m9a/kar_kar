import telebot
import webbrowser
from telebot import types
import sqlite3

token = '7716662637:AAFGd3wzQ1F_TsOlzIfdG3JOxj7zg9PwUkk'
bot = telebot.TeleBot(token)

name1 = ''


@bot.message_handler(commands=['reg'])
def reg(message):
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name varchar(50), password varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Введите имя')
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    global name1
    name1 = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, get_password)


def get_password(message):
    password1 = message.text.strip()
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, password) VALUES ('%s', '%s')" % (name1, password1))
    conn.comit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Список пользователей', callback_data='users')
    markup.add(button)
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup)


@bot.message_handler(commands=['start'])
def new(message):
    markup = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton('зайти в ютуб')
    button2 = types.KeyboardButton('что с дискордом')
    button3 = types.KeyboardButton('где кеша')
    markup.add(button)
    markup.add(button2)
    markup.add(button3)
    bot.send_message(message.chat.id, 'Введи команду')
    bot.register_next_step_handler(message, on_click)


@bot.message_handler(commands=['hello'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Перейти на сайт', url='youtube.com')
    button2 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.add(button, button2)
    bot.send_message(message.chat.id, message.from_user.first_name, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_func(callback):
    bot.edit_message_text('Здравствуй!', callback.message.chat.id, callback.message.id - 2)


@bot.message_handler(commands=['info'])
def start(message):
    bot.send_message(message.chat.id,
                     "Вопросы пиши с вопросительным знаком. Команды пиши с маленькой буквы. Обычные сообщения - без разницы с какой буквы, без орфографических знаков.",
                     parse_mode='html')


@bot.message_handler(commands=['site', 'website'])
def start(message):
    webbrowser.open('youtube.com')


@bot.message_handler()
def start(message):
    if message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока')
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id, 'У меня всё отлично, как у тебя?')
    elif message.text.lower() == 'ты тут?':
        bot.send_message(message.chat.id, 'Я всегда здесь...')
    elif message.text.lower() == 'ты умный?':
        bot.send_message(message.chat.id, 'Возможно, частично.')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, 'Клёвое фото')


@bot.message_handler(content_types=['sticker', 'voice'])
def get_photo(message):
    markup = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton('зайти в ютуб')
    button2 = types.KeyboardButton('что с дискордом')
    button3 = types.KeyboardButton('где кеша')
    markup.add(button)
    markup.add(button2)
    markup.add(button3)
    bot.send_message(message.chat.id, "Забавно", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'зайти в ютуб':
        webbrowser.open('youtube.com')
    elif message.text == 'что с дискордом':
        pass

import telebot
import webbrowser
from telebot import types
import sqlite3

token = '7716662637:AAFGd3wzQ1F_TsOlzIfdG3JOxj7zg9PwUkk'
bot = telebot.TeleBot(token)

name1 = ''


@bot.message_handler(commands=['reg'])
def reg(message):
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name varchar(50), password varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Введите имя')
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    global name1
    name1 = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, get_password)


def get_password(message):
    password1 = message.text.strip()
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, password) VALUES (%5, %5)' % (name1, password1))
    conn.comit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Список пользователей', callback_data='users')
    markup.add(button)
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup)


@bot.message_handler(commands=['start'])
def new(message):
    markup = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton('зайти в ютуб')
    button2 = types.KeyboardButton('что с дискордом')
    button3 = types.KeyboardButton('где кеша')
    markup.add(button)
    markup.add(button2)
    markup.add(button3)
    bot.send_message(message.chat.id, 'Введи команду')
    bot.register_next_step_handler(message, on_click)


@bot.message_handler(commands=['hello'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Перейти на сайт', url='youtube.com')
    button2 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.add(button, button2)
    bot.send_message(message.chat.id, message.from_user.first_name, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_func(callback):
    bot.edit_message_text('Здравствуй!', callback.message.chat.id, callback.message.id - 2)


@bot.message_handler(commands=['info'])
def start(message):
    bot.send_message(message.chat.id,
                     "Вопросы пиши с вопросительным знаком. Команды пиши с маленькой буквы. Обычные сообщения - без разницы с какой буквы, без орфографических знаков.",
                     parse_mode='html')


@bot.message_handler(commands=['site', 'website'])
def start(message):
    webbrowser.open('youtube.com')


@bot.message_handler()
def start(message):
    if message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока')
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id, 'У меня всё отлично, как у тебя?')
    elif message.text.lower() == 'ты тут?':
        bot.send_message(message.chat.id, 'Я всегда здесь...')
    elif message.text.lower() == 'ты умный?':
        bot.send_message(message.chat.id, 'Возможно, частично.')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, 'Клёвое фото')


@bot.message_handler(content_types=['sticker', 'voice'])
def get_photo(message):
    markup = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton('зайти в ютуб')
    button2 = types.KeyboardButton('что с дискордом')
    button3 = types.KeyboardButton('где кеша')
    markup.add(button)
    markup.add(button2)
    markup.add(button3)
    bot.send_message(message.chat.id, "Забавно", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'зайти в ютуб':
        webbrowser.open('youtube.com')
    elif message.text == 'что с дискордом':
        pass


def on_click(message):
    if message.text == 'зайти в ютуб':
        webbrowser.open('youtube.com')
    elif message.text == 'что с дискордом':
        pass

import telebot
from currency_converter import CURRENCY_FILE, CurrencyConverter
from telebot import types
import requests
import json

api_key = '69acd89cdb6c4e0d924214412240111'
city = ''
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

token = '7716662637:AAFGd3wzQ1F_TsOlzIfdG3JOxj7zg9PwUkk'
bot = telebot.TeleBot(token)
amount = 0
convertor = CurrencyConverter


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Введите значение.')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
        if amount > 0:
            markup = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton('USD/EUR', callback_data='USD/EUR')
            button2 = types.InlineKeyboardButton('EUR/USD', callback_data='EUR/USD')
            button3 = types.InlineKeyboardButton('another', callback_data='another')
            markup.add(button, button2)
            markup.add(button3)

            bot.send_message(message.chat.id, 'Выберите валюту:', reply_markup=markup)
            bot.register_next_step_handler(message, send_currency)
        else:
            bot.reply_to(message, "Неверный формат. Введите положительно число:")
            bot.register_next_step_handler(message, send_currency)
    except ValueError:
        bot.reply_to(message, "Неверный формат. Введите число.")
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def send_currency(call):
    if call.data != "another":
        values = call.data.split('/')
        result = convertor.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f"Получившееся значение: {result).Можете ввести число заново:")
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, f"Введите пару валют через слэш")
        bot.register_next_step_handler(call.message, another_currency)


def another_currency(message):
    try:
        values = message.text.upper().split('/')
        result = convertor.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f"Получившееся значение: {result},")
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.reply_to(message, "Неверный формат. Введите положительно число:")
        bot.register_next_step_handler(message, another_currency)


@bot.message_handler(content_types=['text'])
def get_weather(message):
    global city
    city = message.text.strip()
    try:
        result = requests.get(url)
        data = json.loads(result.text)

        bot.reply_to(message, f"Погода: {data['main']['temp']}")
    except TimeoutError:
        bot.reply_to(message, 'Время ожидания истекло')


bot.infinity_polling()