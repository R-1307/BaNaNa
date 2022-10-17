import telebot
import re
bot = telebot.TeleBot('5447167820:AAFJuMm9pRhlJn4Wd3cX7skHNNWRZhBdTZY')


@bot.message_handler()
def get_user_text(message):
    if re.search(r'\bганж\b', message.text.lower()):
        bot.send_message(message.chat.id, "Г а н ж П и д о р")
    if re.search(r'\bутро\b', message.text.lower()):
        bot.send_message(message.chat.id, "Х У Ю Т Р О!")
        bot.send_message(message.chat.id, "Держи банан!")
        bot.send_message(message.chat.id, '\U0001F34C')
        bot.send_message(message.chat.id, "псина")
    if re.search(r'\bбанан\b', message.text.lower()):
          bot.send_message(message.chat.id, '\U0001F34C')
    if re.search(r'\bbanana\b', message.text.lower()):
        bot.send_message(message.chat.id, 'BANANA!!!!')
        bot.send_message(message.chat.id, '\U0001F34C')
        bot.send_message(message.chat.id, '\U0001F34C')
        bot.send_message(message.chat.id, '\U0001F34C')
    if message.text == '\U0001F34C':
        bot.send_message(message.chat.id, '\U0001F34C')
    if message.from_user.id in [241957427,-1001009232144,-1001633241826,-1001335343936,-1001013523094,-1001509508777]:
        voice = open('/home/helldude/banana/fart3.ogg', 'rb')
        bot.send_voice(message.chat.id, voice)

bot.polling(none_stop=True)

