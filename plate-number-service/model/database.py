from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from conf import DATABASE


db_url = create_engine(DATABASE, pool_pre_ping=True, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_url)
Base = declarative_base()

# Base.metadata.create_all(bind=db_url)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()