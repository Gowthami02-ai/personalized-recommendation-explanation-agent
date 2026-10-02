from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "personalized-recommendation-explanation-agent"
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"
    embedding_model: str = "text-embedding-3-small"

    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/reco_agent"
    redis_url: str = "redis://localhost:6379/0"
    chroma_url: str = "http://localhost:8001"
    chroma_collection_name: str = "project_knowledge"

    cors_origins: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

settings = Settings()
