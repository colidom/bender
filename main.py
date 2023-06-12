import telebot

api = "6225579104:AAHyGu3zfApAUT68SyhOcOoeL8zV6SerHMQ"
bender = telebot.TeleBot(api)

@bender.message_handler(commands = ["help", "start"])
def send_message(message):
    bender.reply_to(message, "Hi there!")

bender.polling()
