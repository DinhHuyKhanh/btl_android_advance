from sqlalchemy.orm.session import Session
from model.database import SessionLocal
from model.models import User

class UserRepository():

    def __init__(self) -> None:
        self.db = SessionLocal()

    def get_all_users(self):
        return self.db.query(User).all()