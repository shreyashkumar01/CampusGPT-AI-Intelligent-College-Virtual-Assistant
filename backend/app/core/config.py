import os
from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    SECRET_KEY: str = "change_this_secret_key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str = "sqlite:///./campusgpt.db"
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    SENTENCE_TRANSFORMERS_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    CHROMA_DB_PATH: str = "./chroma_db"

    class Config:
        env_file = ".env"

settings = Settings()
