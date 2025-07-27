# Standard library imports
import os
import json

# Third-party imports
from dotenv import find_dotenv, load_dotenv

class Settings:
    """
    Settings class to manage configuration and environment variables for the application.
    """

    # Load environment variables from a .env file if it exists
    load_dotenv(find_dotenv())

    # Path to the logs directory, defaulting to 'logs'
    LOGS_DIR = os.getenv('LOGS_DIR', 'logs')

    # Path to the logging configuration file, defaulting to 'logging.conf'
    LOGGING_CONFIG = os.getenv('LOGGING_CONFIG', 'logging.conf')

    # Path to the templates directory, defaulting to 'templates'
    TEMPLATES_DIR = os.getenv('TEMPLATES_DIR', 'templates')

    # Path to the index html file, defaulting to 'convert_images.html'
    INDEX_HTML = os.getenv('INDEX_HTML', 'convert_images.html')

    class Config:
        """
        Configuration settings for handling the environment file.
        """
        # Path to the .env file
        env_file = ".env"

        # Encoding used for the .env file
        env_file_encoding = 'utf-8'

# Instantiate the settings object to be used across the application
settings = Settings()
