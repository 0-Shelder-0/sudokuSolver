from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = environ.get('DATABASE_URL')
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
