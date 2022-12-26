import telebot
import re
bot = telebot.TeleBot('5447167820:AAFJuMm9pRhlJn4Wd3cX7skHNNWRZhBdTZY')


@bot.message_handler()
def get_user_text(message):
    if re.search(r'[г]анж', message.text.lower()):
#       bot.send_message(message.chat.id, "Г а н ж П и д о р")
        sti = open('/home/helldude/banana/kolia.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
    if re.search(r'[у]тро', message.text.lower()):
        bot.send_message(message.chat.id, "Х У Ю Т Р О!")
        bot.send_message(message.chat.id, "Держи банан!")
        bot.send_message(message.chat.id, '\U0001F34C')
        bot.send_message(message.chat.id, "псина")
    if re.search(r'[б]анан', message.text.lower()):
          bot.send_message(message.chat.id, '\U0001F34C')
    if re.search(r'[b]anana', message.text.lower()):
        bot.send_message(message.chat.id, 'BANANA!!!!')
        bot.send_message(message.chat.id, '\U0001F34C')
        bot.send_message(message.chat.id, '\U0001F34C')
        bot.send_message(message.chat.id, '\U0001F34C')
    if message.text == '\U0001F34C':
        bot.send_message(message.chat.id, '\U0001F34C')
    if message.from_user.id in [241957427]:
        voice = open('/home/helldude/banana/fart3.ogg', 'rb')
        bot.send_voice(message.chat.id, voice)

    if re.search(r'[д]еменц', message.text.lower()):
        bot.send_message(message.chat.id, 'О')
        bot.send_message(message.chat.id, 'У меня есть шутка про деменцию!')
        bot.send_message(message.chat.id, 'Но ее так не понять')
        bot.send_message(message.chat.id, 'Ее прочувствовать надо!')
    if re.search(r'[а]льцг', message.text.lower()):
        bot.send_message(message.chat.id, 'О')
        bot.send_message(message.chat.id, 'У меня есть шутка про альцгеймер!')
        bot.send_message(message.chat.id, 'Но ее так не понять')
        bot.send_message(message.chat.id, 'Ее прочувствовать надо!')
bot.polling(none_stop=True)


