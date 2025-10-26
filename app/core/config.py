from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_ENV: str = "local"
    APP_PORT: int = 8000
    JWT_SECRET: str = "CHANGE_ME"
    JWT_ALG: str = "HS256"
    ACCESS_TOKEN_MIN: int = 20

    class Config:
        env_file = ".env"

settings = Settings()
