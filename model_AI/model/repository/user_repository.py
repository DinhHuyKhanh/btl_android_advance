from sqlalchemy.orm.session import Session
from model.database import SessionLocal, get_db
from model.models import DbUser

class UserRepository():

    def __init__(self) -> None:
        self.db = SessionLocal()

    def get_all_users(self):
        return self.db.query(DbUser).all()