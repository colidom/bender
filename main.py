import telebot
from bot.utils import load_token
from bot.handlers import register_handlers

def main():
    """Configurar e iniciar el bot."""
    token = load_token()
    application = telebot.TeleBot(token)

    register_handlers(application)

    print("Corriendo Bot... Presiona Ctrl+C para detenerlo.")
    application.polling()

if __name__ == "__main__":
    main()
