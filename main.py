import telebot
from bot.utils import load_token

def main():
    """Configurar e iniciar el bot."""
    token = load_token()
    application = telebot.TeleBot(token)

    @application.message_handler(commands=["hola", "start"])
    def send_message(message):
        application.reply_to(message, "Hi there!")

    print("Corriendo Bot... Presiona Ctrl+C para detenerlo.")
    application.polling()

if __name__ == "__main__":
    main()
