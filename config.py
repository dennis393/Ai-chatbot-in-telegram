from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENROUTER_TOKEN: str
    TG_TOKEN: str
    MY_TG_ID: int
    DB_USER: str
    DB_NAME: str
    DB_HOST: str
    DB_PASSWORD: str
    DB_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    
    model_config = SettingsConfigDict(env_file=".env", exta="ignore")

settings = Settings()
    