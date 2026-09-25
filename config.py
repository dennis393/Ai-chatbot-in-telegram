from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENROUTER_TOKEN: str
    TG_TOKEN: str
    WEBHOOK_URL: str
    WEBHOOK_PATH: str="/webhook"
    WEBHOOK_TOKEN: str="aboba6769"
    
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore")

settings = Settings()
    