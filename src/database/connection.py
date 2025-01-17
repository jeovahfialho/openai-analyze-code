from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.config import get_settings

settings = get_settings()

# Create SQLAlchemy engine
engine = create_engine(settings.DATABASE_URL)

# Create sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

def get_db_session():
    """
    Get database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()