import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.utils import load_token
from bot.handlers import register_handlers


def main():
    """Configurar e iniciar el bot."""
    token = load_token()
    application = telebot.TeleBot(token)

    @application.message_handler(commands=["hola", "start"])
    def send_message(message):
        """Responde a los comandos /hola y /start."""
        application.reply_to(message, "¡Hola! Estoy aquí para ayudar.")

    @application.message_handler(content_types=["new_chat_members"])
    def welcome_new_member(message):
        """Saluda a los nuevos miembros del grupo y les envía un botón."""
        for new_member in message.new_chat_members:
            chat_id = message.chat.id
            user_first_name = new_member.first_name

            # Crear un botón inline
            markup = InlineKeyboardMarkup()
            button = InlineKeyboardButton("Soy un humano", callback_data="verify_human")
            markup.add(button)

            # Enviar mensaje de bienvenida con el botón
            application.send_message(
                chat_id,
                f"¡Bienvenido, {user_first_name}! Haz clic en el botón de abajo para confirmar que eres humano.",
                reply_markup=markup,
            )

    @application.callback_query_handler(func=lambda call: call.data == "verify_human")
    def handle_verification(call):
        """Maneja la verificación del usuario cuando presiona el botón."""
        user_name = call.from_user.first_name
        chat_id = call.message.chat.id

        # Responder al usuario y eliminar el mensaje del botón
        application.send_message(
            chat_id,
            f"¡Gracias por verificarte, {user_name}! Ya puedes interactuar en el grupo.",
        )
        application.delete_message(chat_id, call.message.message_id)

    print("Corriendo Bot... Presiona Ctrl+C para detenerlo.")
    application.polling()


if __name__ == "__main__":
    main()
