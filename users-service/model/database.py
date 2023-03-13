from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)


DATABASE = {
    'drivername': 'mysql+mysqlconnector',
    'username': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host':  os.getenv('DB_HOST'),
    'port':  os.getenv('DB_PORT'),
    'database':  os.getenv('DB_DATABASE')
}

print(DATABASE)

db_url = create_engine(URL(**DATABASE), pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_url)
Base = declarative_base()

# Base.metadata.create_all(bind=db_url)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()