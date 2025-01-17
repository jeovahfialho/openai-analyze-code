from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/codeadvisor"
    
    # Redis settings
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # API settings
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = True
    PROJECT_NAME: str = "Python Code Advisor"
    VERSION: str = "1.0.0"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()