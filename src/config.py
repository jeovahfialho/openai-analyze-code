from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str = "postgresql://user:password@db:5432/codeadvisor"
    POSTGRES_USER: str = "user"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "codeadvisor"
    
    # Redis settings
    REDIS_URL: str = "redis://redis:6379/0"
    
    # API settings
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = True
    PROJECT_NAME: str = "Python Code Advisor"
    VERSION: str = "1.0.0"

    # Security settings
    SECRET_KEY: str = "your-super-secret-key-here"
    
    # Environment settings
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        extra = "allow"  # Isso permite campos extras se quiser ser mais flexível

@lru_cache()
def get_settings():
    return Settings()