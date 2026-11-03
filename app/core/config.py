from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    PROJECT_NAME: str = "curriculo-ats-api"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    ENV: str = "development"
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:4200",
        "http://127.0.0.1:4200",
    ]
    RATE_LIMIT: str = "60/minute"


settings = Settings()
