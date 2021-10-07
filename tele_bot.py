import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import datetime

date = datetime.datetime.now()
date = date.date()

bot = telebot.TeleBot("2025764749:AAEhrRBChM1kh0xbH4N31Kl6ISgsD9cY2MI")
aries_url = 'https://horo.mail.ru/prediction/aries/today/' # url страницы
taurus_url = 'https://horo.mail.ru/prediction/taurus/today/'
gemini_url = "https://horo.mail.ru/prediction/gemini/today/"
cancer_url = "https://horo.mail.ru/prediction/cancer/today/"
leo_url = "https://horo.mail.ru/prediction/leo/today/"
virgo_url = "https://horo.mail.ru/prediction/virgo/today/"
libra_url = "https://horo.mail.ru/prediction/libra/today/"
scorpio_url = "https://horo.mail.ru/prediction/scorpio/today/"
sagittarius_url = "https://horo.mail.ru/prediction/sagittarius/today/"
capricorn_url = "https://horo.mail.ru/prediction/capricorn/today/"
aquarius_url = "https://horo.mail.ru/prediction/aquarius/today/"
pisces_url = "https://horo.mail.ru/prediction/pisces/today/"


keyboard = types.InlineKeyboardMarkup()
key_aries = types.InlineKeyboardButton(text='Овен', callback_data='aries_zodiac')
keyboard.add(key_aries)
key_taurus = types.InlineKeyboardButton(text='Телец', callback_data='taurus_zodiac')
keyboard.add(key_taurus)
key_gemini = types.InlineKeyboardButton(text='Близнецы', callback_data='gemini_zodiac')
keyboard.add(key_gemini)
key_cancer = types.InlineKeyboardButton(text='Рак', callback_data='cancer_zodiac')
keyboard.add(key_cancer)
key_leo = types.InlineKeyboardButton(text='Лев', callback_data='leo_zodiac')
keyboard.add(key_leo)
key_virgo = types.InlineKeyboardButton(text='Дева', callback_data='virgo_zodiac')
keyboard.add(key_virgo)
key_libra = types.InlineKeyboardButton(text='Весы', callback_data='libra_zodiac')
keyboard.add(key_libra)
key_scorpio = types.InlineKeyboardButton(text='Скорпион', callback_data='scorpio_zodiac')
keyboard.add(key_scorpio)
key_sagittarius = types.InlineKeyboardButton(text='Стрелец', callback_data='sagittarius_zodiac')
keyboard.add(key_sagittarius)
key_capricorn = types.InlineKeyboardButton(text='Козерог', callback_data='capricorn_zodiac')
keyboard.add(key_capricorn)
key_aquarius = types.InlineKeyboardButton(text='Водолей', callback_data='aquarius_zodiac')
keyboard.add(key_aquarius)
key_pisces = types.InlineKeyboardButton(text='Рыбы', callback_data='pisces_zodiac')
keyboard.add(key_pisces)

keyboard1 = types.InlineKeyboardMarkup()
key_back = types.InlineKeyboardButton(text='Вернуться', callback_data='back_to_zodiac')
keyboard1.add(key_back)

def req(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    return soup.find_all('div', {'class': 'article__text'})








@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, f"Привет, сейчас я расскажу тебе гороскоп на {date}.")
        bot.send_message(message.from_user.id, text='Выбери знак зодиака', reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start чтобы начать")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "aries_zodiac":
        passage = req(aries_url)
        msg = "♈Овен♈\n"
        for item in passage:
            msg += item.text
            break
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "taurus_zodiac":
        passage = req(taurus_url)
        msg = "♉Телец♉\n"
        for item in passage:
            msg += item.text
            break
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "gemini_zodiac":
        passage = req(gemini_url)
        msg = "♊Близнецы♊\n"
        for item in passage:
            msg += item.text
            break
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "cancer_zodiac":
        passage = req(cancer_url)
        msg = "♋Рыбы♋\n"
        for item in passage:
            msg += item.text
            break
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "leo_zodiac":
        passage = req(leo_url)
        msg = "♌Лев♌\n"
        for item in passage:
            msg += item.text
            break
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "virgo_zodiac":
        passage = req(virgo_url)
        msg = "♍Дева♍\n"
        for item in passage:
            msg += item.text
            break
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "libra_zodiac":
        passage = req(libra_url)
        msg = "♎Весы♎\n"
        for item in passage:
            msg += item.text
            break
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "scorpio_zodiac":
        passage = req(scorpio_url)
        msg = "♏Скорпион♏\n"
        for item in passage:
            msg += item.text
            break
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "sagittarius_zodiac":
        passage = req(sagittarius_url)
        msg = "♐Стрелец♐\n"
        for item in passage:
            msg += item.text
            break
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "capricorn_zodiac":
        passage = req(capricorn_url)
        msg = "♑Козерог♑\n"
        for item in passage:
            msg += item.text
            break
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "aquarius_zodiac":
        passage = req(aquarius_url)
        msg = "♒Володей♒\n"
        for item in passage:
            msg += item.text
            break
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "pisces_zodiac":
        passage = req(pisces_url)
        msg = "♓Рыбы♓\n"
        for item in passage:
            msg += item.text
            break
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "back_to_zodiac":
        bot.send_message(call.message.chat.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
        return
    #bot.send_message(call.message.chat.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    bot.send_message(call.message.chat.id, text="Вернуться к выбору знака зодиака", reply_markup=keyboard1)

bot.polling(none_stop=True, interval=0)
#if __name__ == '__main__':
#        bot.infinity_polling()