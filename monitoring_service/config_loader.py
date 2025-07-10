"""
config_loader.py

Provides the ConfigLoader class for loading, validating, and exposing configuration values
from a .env file and a config.json file. Used to supply runtime settings for the application.

Classes:
    ConfigLoader

Usage:
    config = ConfigLoader(logger)
    settings = config.as_dict()
"""

import os
import json
from dotenv import load_dotenv


class ConfigLoader:
    """
    Handles loading and validating environment variables and JSON configuration.

    Uses `python-dotenv` to load values from a `.env` file and reads runtime settings
    from a `config.json` file. Ensures required variables are present and provides
    access to all configuration data via the `as_dict()` method.

    Args:
        logger (logging.Logger): Logger used to report missing config or file errors.

    Raises:
        EnvironmentError: If required environment variables are missing.
        FileNotFoundError: If the configuration file cannot be found.
    """

    def __init__(self, logger):
        load_dotenv()
        self.token = os.getenv("ACCESS_TOKEN")
        self.server = os.getenv("THINGSBOARD_SERVER")
        self.config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
        self.logger = logger

        try:
            with open(self.config_path) as config_file:
                self.config = json.load(config_file)
        except FileNotFoundError as e:
            self.logger.error(f"Could not load config file {e}")
            raise

        self._validate_or_raise()

    def as_dict(self):
        """
        Gets the token, server and config values
        :return: a dict containing the configuration values
        """
        return {
            "token": self.token,
            "server": self.server,
            "config": self.config
        }

    def _validate_or_raise(self):
        missing = []
        if not self.token:
            missing.append("ACCESS_TOKEN")
        if not self.server:
            missing.append("THINGSBOARD_SERVER")
        if missing:
            error_message = f"Missing required environment variables: {', '.join(missing)}"
            self.logger.error(error_message)
            raise EnvironmentError(error_message)
