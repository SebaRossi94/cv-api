from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    app_name: str = "CV API"
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "sqlite:///cv.db")


settings = Settings()