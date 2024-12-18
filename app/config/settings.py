"""This module contains the settings for the application."""

from functools import lru_cache
import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """The settings for the application."""

    # Security
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    HASHING_ALGORITHM: str = os.environ.get("HASHING_ALGORITHM")

    # DB Settings
    POSTGRES_DATABASE_URL: str = os.environ.get("POSTGRES_DATABASE_URL")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Opcional: tiempo de expiración del token

    # MQTT Settings

    MQTT_BROKER: str = os.environ.get("MQTT_BROKER")
    MQTT_PORT: int = os.environ.get("MQTT_PORT")

    class Config:
        """The configuration for the settings."""

        env_file = ".env"


@lru_cache
def get_settings():
    """This function returns the settings obj for the application."""
    return Settings()
