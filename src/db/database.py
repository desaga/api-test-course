# src/db/database.py
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

load_dotenv()  # Завантаження змінних з .env

class Database:
    def __init__(self):
        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            raise ValueError("DATABASE_URL not found in .env file")

        self.engine = create_engine(db_url, echo=True)
        self.Session = scoped_session(sessionmaker(bind=self.engine))

    def get_session(self):
        try:
            return self.Session()
        except SQLAlchemyError as e:
            print(f"Database session error: {e}")
            raise

    def close_session(self):
        self.Session.remove()

if __name__ == '__main__':
    db = Database()
    try:
        session = db.get_session()
        result = session.execute(text("SELECT 1"))
        import pdb
        pdb.set_trace()
        assert result.scalar() == 1
        print("Successfully connected to database!")
    except SQLAlchemyError as e:
        print("Database connection error: ")
        print(e)
    finally:
        db.close_session()