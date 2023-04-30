import logging
from util.constants import TableNames
from util.utils import convert_model_to_json
from model.repository.base_repository import BaseRepository
from model.models import UserData
from sqlalchemy import text
import json
logger = logging.getLogger()

class UserRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()

    def get(self, id, filter=None):
        if id is None:
            return None
        if not filter:
            filter = {}

        filter["Id"] = id
        
        user = self.db.query(UserData).filter_by(**filter).first()
        return user
        
    def get_by(self, filter):
        user = self.db.query(UserData).filter_by(**filter).first()
        return user
        
    def get_by_and_update(self, filter, update):
        data = self.db.query(UserData).filter_by(**filter)
        count = data.update(update)
        self.db.commit()
        return count
    
    def update(self, id, filter):
        data = self.db.query(UserData).filter_by(Id=id)
        count = data.update(filter)
        self.db.commit()
        return count

    def get_all_users(self, limit, offset, sort):
        with self.db as session: 
            result = session.execute(text(
                f"""
                SELECT Id, FullName, PhoneNumber, Email, PersonalNumber, Address, activate,
                Coin, BirthDay
                FROM {TableNames.USER_DATA.value}
                ORDER BY Id {sort}
                LIMIT :limit 
                OFFSET :offset
                """
            ).params(
                limit=limit,
                offset=offset*limit,
            ))
            rows = [dict(row) for row in result.fetchall()]
            return rows

    def create(self, user_dict):
        self.db.add(user_dict)
        self.db.commit()
        self.db.refresh(user_dict)
        return convert_model_to_json(user_dict, UserData)
    
    def get_user_by_email(self, email: str):
        stored_user = self.db.query(UserData).filter(UserData.Email == email).first()
        if stored_user:
            return convert_model_to_json(stored_user, UserData)
        return None
    
    def count_user(self):
        count = self.db.query(UserData).count()
        if not count: 
            count = 0
        return count
