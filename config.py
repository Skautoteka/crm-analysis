from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    backend_url: str = "http://localhost:3000/api/"
