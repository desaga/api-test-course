# src/db/dal/users_dal.py

from sqlalchemy import text
from src.db.database import Database

def user_exists(email):
    db = Database()
    session = db.Session()
    # import pdb; pdb.set_trace()

    try:
        result = session.execute(
            text("SELECT 1 FROM wp_users WHERE user_email = :email"),
            {"email":email}
        ).scalar()
        if result:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def get_existed_customer_email():
    db = Database()
    session = db.Session()

    try:
        result = session.execute(
            text("SELECT user_email FROM wp_users LIMIT 1")
        )

        result = result.scalar()
        # import pdb; pdb.set_trace()
        if result:
            return result
        else:
            raise Exception("No user exists with in database")
    except Exception as e:
        print(e)
        return False
