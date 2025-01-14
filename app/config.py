import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    hostname: str = os.environ.get("HOSTNAME", "localhost")
    backend_url: str = f"http://{hostname}:3000/api/"

    model_config = SettingsConfigDict(env_file=".env")
