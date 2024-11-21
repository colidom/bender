import os
from dotenv import load_dotenv

def load_token():
    """Returns the API TOKEN loaded from the .env file.

    Raises:
        ValueError: If the API_TOKEN is not found in the .env file.
    """
    load_dotenv()
    token = os.getenv('API_TOKEN')

    if token:
        print(f"¡Cargado token {token} correctamente!")
        return token
    else:
        raise ValueError("No se pudo cargar el token. Asegúrate de que esté definido en el archivo .env.")
