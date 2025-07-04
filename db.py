from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

import os

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

print("Connecting to:", SQLALCHEMY_DATABASE_URL)
#for connnection with postgres use:
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#for the connection with sqlite: use the below one:
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()