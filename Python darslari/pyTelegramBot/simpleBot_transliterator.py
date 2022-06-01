from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '5427270655:AAGE2l0T5WV4gPdeib5allkKS7AAgCsMC-U'
bot = telebot.TeleBot(token = TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = (
        message.from_user.username
    )
    answer = f"Assalomu alaykum {username}! \nXush keldingiz!"
    bot.reply_to(message, answer)


@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)

    bot.reply_to(message, answer(msg))

bot.polling()
