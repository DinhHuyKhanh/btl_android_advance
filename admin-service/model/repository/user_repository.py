import bcrypt
from sqlalchemy.orm.session import Session
from model.database import SessionLocal
from model.models import User




class UserRepository():

    def __init__(self) -> None:
        self.db = SessionLocal()

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


    def check_password(self, password: str, encoded_pwd) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), encoded_pwd.encode('utf-8'))

    def get_all_users(self):
        return self.db.query(User).all()

    def create_user(self, user: User) -> User:
        user.Password = self.hash_password(user.Password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.Email == email).first()

    def authenticate_user(self, email: str, password: str) -> User:
        user = self.get_user_by_email(email)
        if not user:
            return None
        if not user.check_password(password, user.Password):
            return None
        return user
