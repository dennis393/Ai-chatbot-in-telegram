from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENROUTER_TOKEN: str
    TG_TOKEN: str
    DB_USER: str
    DB_NAME: str
    DB_HOST: str
    DB_PASSWORD: str
    DB_PORT: str
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
    