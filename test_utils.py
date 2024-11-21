# test_utils.py
import os
import unittest
from unittest.mock import patch, MagicMock
from dotenv import load_dotenv
from bot.utils import load_token

class TestLoadToken(unittest.TestCase):

    @patch('os.getenv')
    @patch('bot.utils.load_dotenv')
    def test_load_token_success(self, mock_load_dotenv, mock_getenv):
        """Test that load_token returns the API_TOKEN when it exists."""
        mock_getenv.return_value = 'test_token'
        token = load_token()
        self.assertEqual(token, 'test_token')
        mock_load_dotenv.assert_called_once()
        mock_getenv.assert_called_once_with('API_TOKEN')

    @patch('os.getenv')
    @patch('bot.utils.load_dotenv')
    def test_load_token_failure(self, mock_load_dotenv, mock_getenv):
        """Test that load_token raises ValueError when API_TOKEN is missing."""
        mock_getenv.return_value = None
        with self.assertRaises(ValueError) as context:
            load_token()
        
        self.assertEqual(str(context.exception), "No se pudo cargar el token. Asegúrate de que esté definido en el archivo .env.")
        mock_load_dotenv.assert_called_once()
        mock_getenv.assert_called_once_with('API_TOKEN')

if __name__ == '__main__':
    unittest.main()
