from util.utils import convert_model_to_json
from model.repository.base_repository import BaseRepository
from sqlalchemy.orm.session import Session
from model.database import SessionLocal, get_db
from model.models import UserData

class UserRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__()

    def get_all_users(self):
        return self.db.query(UserData).all()
    
    def create(self, user_dict):
        new_user = UserData(**user_dict)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return convert_model_to_json(new_user, UserData), 1, "success"
    
    def get_user_by_email(self, email: str):
        stored_user = self.db.query(UserData).filter(UserData.Email == email).first()
        if stored_user:
            return convert_model_to_json(stored_user, UserData), 1, "success"
        return None, -1, 'email not exists'

