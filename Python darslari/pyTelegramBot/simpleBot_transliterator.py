from transliterate import to_cyrillic, to_latin
from pyTelegramBotAPI import telebot

token = '5427270655:AAGE2l0T5WV4gPdeib5allkKS7AAgCsMC-U'
bot = telebot.TeleBot(token, parse_mode = None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = "Assalomu alaykum\nXush keldingiz!"
    bot.reply_to(message, answer)

@bot.message_handler(func = lambda message: True)
def echo_all(message):
    msg = message.text
    answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)

    bot.reply_to(message, answer)

bot.polling()