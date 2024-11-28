import telebot

def register_handlers(application):
    """Registra todos los manejadores del bot."""

    @application.message_handler(func=lambda message: 'hola' in message.text.lower())
    def greet_user(message):
        """Saluda al usuario que mencionó 'hola'."""
        user_first_name = message.from_user.first_name
        greeting_message = f"¡Hola {user_first_name}! 👋 Bienvenido"
        application.send_message(message.chat.id, greeting_message)
