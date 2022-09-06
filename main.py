import telebot

bot = telebot.TeleBot('5447167820:AAFJuMm9pRhlJn4Wd3cX7skHNNWRZhBdTZY')


@bot.message_handler()
def get_user_text(message):
    if message.text == "Ганж" or message.text == "Коля" or message.text == "ганж" or message.text == "Ганж)":
        bot.send_message(message.chat.id, "Г а н ж П и д о р")
    if message.text == "Доброе утро" or message.text == "Доброе утро!" or message.text == "доброе утро":
        bot.send_message(message.chat.id, "Х У Ю Т Р О!")
        bot.send_message(message.chat.id, "Держи банан!")
        bot.send_message(message.chat.id, '\U0001F34C')
    if message.text == "держи банан" or message.text == "Держи банан" or message.text == "Держи Банан" or message.text == "Держи банан!" or message.text == "держи банан)":
          bot.send_message(message.chat.id, '\U0001F34C')
    if message.text == message.text == "BANANA!":
        bot.send_message(message.chat.id, 'BANANA!!!!')
        bot.send_message(message.chat.id, '\U0001F34C')
        bot.send_message(message.chat.id, '\U0001F34C')
        bot.send_message(message.chat.id, '\U0001F34C')
    if message.text == '\U0001F34C':
        bot.send_message(message.chat.id, '\U0001F34C')

bot.polling(none_stop=True)
