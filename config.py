from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    backend_url: str = "http://localhost:3000/api/"

    model_config = SettingsConfigDict(env_file=".env")
