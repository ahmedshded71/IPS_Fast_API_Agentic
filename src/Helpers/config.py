from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
class Settings(BaseSettings):
    GOOGLE_API_KEY: str
    OPENAI_API_KEY: str
    APP_NAME:str
    APP_VERSION:str


    model_config = SettingsConfigDict(env_file=".env")

def get_settings():
    return Settings()





