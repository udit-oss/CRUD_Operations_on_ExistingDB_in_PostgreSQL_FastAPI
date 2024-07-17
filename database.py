from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgresql@localhost:5432/Supermart_DB"

# Creates SQLAlchemy Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Base class for models
Base = declarative_base()

# Create a configured session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
