"""Configuration centralisée, lue depuis l'environnement et le fichier .env racine."""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[3]
ENV_FILE = PROJECT_ROOT / ".env"


class Settings(BaseSettings):
    app_name: str = "Plateforme de productivité étudiante"
    environment: str = "development"
    backend_host: str = "0.0.0.0"
    backend_port: int = 8001
    log_level: str = "INFO"
    cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173"
    database_url: str = (
        "postgresql+psycopg://pfa_user:change_me@127.0.0.1:5433/pfa_productivity"
    )

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def cors_origin_list(self) -> list[str]:
        origins = [item.strip() for item in self.cors_origins.split(",") if item.strip()]
        return origins or ["http://localhost:5173", "http://127.0.0.1:5173"]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
