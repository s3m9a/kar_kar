import aiogram
import asyncio
import logging
from aiogram import Dispatcher, types, Bot
from aiogram.filters.command import Command
from pyexpat.errors import messages
from telebot.types import WebAppData, WebAppInfo

token = '7716662637:AAFGd3wzQ1F_TsOlzIfdG3JOxj7zg9PwUkk'
bot = Bot(token=token)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(Command('start'))
async def start(message: types.Message):
    # but1 = types.InlineKeyboardButton(text='Перейти на сайт', url = 'youtube.com')
    # but2 = types.InlineKeyboardButton(text='Отправить трек', callback_data = 'send_track')
    # but3 = types.InlineKeyboardButton(text='Моё имя', callback_data = 'user_name')
    # markup = types.InlineKeyboardMarkup(inline_keyboard=[[but1], [but2], [but3]])




    #but = types.InlineKeyboardButton(text="site", url = "youtube.com")
    #but2 = types.InlineKeyboardButton(text="Привет", callback_data = "Привет")
    #markup = types.InlineKeyboardMarkup(inline_keyboard=[[but], [but2]])

    but = types.KeyboardButton(text="site", web_app=WebAppInfo(url="https://html-preview.github.io/?url=https://github.com/s3m9a/kar_kar/blob/main/form.html"))
    but2 = types.KeyboardButton(text="Привет")
    markup1 = types.ReplyKeyboardMarkup(keyboard=[[but], [but2]], one_time_keyboard=True)

    #file = open("files/photo.jpg", 'r+')
    #await message.answer_photo("")
    # message.
    await message.reply('Здравствуй!', reply_markup=markup)


@dp.callback_query()
async def callback(call):
    if call.data == "Привет":
        await call.message.answer(call.data)
    if call.data == "send_track":
        await call.message.answer()
    if call.data == "user_name":
        await call.message.answer()

async def main():
    await dp.start_polling(bot)


if name == "main":
    asyncio.run(main())