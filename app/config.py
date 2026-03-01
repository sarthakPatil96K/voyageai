from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "VoyageAI"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    OPENAI_API_KEY: str | None = None
    DATABASE_URL: str | None = None
    REDIS_URL: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()