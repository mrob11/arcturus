from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Web Event Platform API"
    APP_DESCRIPTION: str = "It's a REST API"
    DATABASE_URL: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
