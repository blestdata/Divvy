import os
import uuid
import datetime as dt
from decimal import Decimal
import sqlite3
from sqlalchemy import create_engine
from contextlib import contextmanager


# SQLite database path in project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "divvy.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

print(f"DB_PATH is {DB_PATH}")


db_engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    pool_size=5,
    max_overflow=10,
    pool_recycle=3600,
    echo=False
)




# with db_engine.connect() as connection:
#     connection.execute("SELECT * FROM my_table")