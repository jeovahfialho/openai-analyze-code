from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Analysis(Base):
    __tablename__ = "analysis_history"

    id = Column(Integer, primary_key=True, index=True)
    code_snippet = Column(String)
    suggestions = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Analysis(id={self.id}, created_at={self.created_at})>"