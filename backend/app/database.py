import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = os.getenv("postgresql://fixit_dbs_wu7y_user:z3h2Pf5HVEwvfPi1nWTYmCcheQ4Qn9rm@dpg-d7ufji3eo5us73e18p6g-a/fixit_dbs_wu7y")

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()