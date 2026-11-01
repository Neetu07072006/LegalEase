
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "LegalEase API"
    app_env: str = "development"
    frontend_url: str = "http://localhost:3000"
    database_url: str = ""
    supabase_url: str = ""
    supabase_key: str = ""
    groq_api_key: str = ""
    groq_model: str = "openai/gpt-oss-120b"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
