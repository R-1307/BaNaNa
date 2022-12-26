import telebot

bot = telebot.TeleBot('5447167820:AAFJuMm9pRhlJn4Wd3cX7skHNNWRZhBdTZY')


@bot.message_handler()
def get_user_text(message):
    if message.text in ["Ганж","Ганж!","Ганж!!", "Ганж!!!", "Коля", "ганж", "Ганж)"]:
        bot.send_message(message.chat.id, "Г а н ж П и д о р")
    elif message.text in ["Доброе утро","Доброе утро!","доброе утро","доброе утро!"]:
        bot.send_message(message.chat.id, "Х У Ю Т Р О!")
        bot.send_message(message.chat.id, "Держи банан!")
        bot.send_message(message.chat.id, '\U0001F34C')
    elif message.text in ["держи банан", "Держи банан","Держи Банан","Держи банан!","держи банан)"]:
          bot.send_message(message.chat.id, '\U0001F34C')
    elif message.text == "BANANA!":
        bot.send_message(message.chat.id, 'BANANA!!!!')
        bot.send_message(message.chat.id, '\U0001F34C')
        bot.send_message(message.chat.id, '\U0001F34C')
        bot.send_message(message.chat.id, '\U0001F34C')
    elif message.text == '\U0001F34C':
        bot.send_message(message.chat.id, '\U0001F34C')
    elif message.from_user.id in [241957427]:
        voice = open('/home/helldude/banana/fart3.ogg', 'rb')
        bot.send_voice(message.chat.id, voice)

bot.polling(none_stop=True)
