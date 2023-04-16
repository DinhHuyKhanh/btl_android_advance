from util.constants import TableNames
from util.utils import convert_model_to_json
from model.repository.base_repository import BaseRepository
from model.models import UserData
from sqlalchemy import text

class UserRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__()

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
                offset=offset,
            ))
            return [dict(row) for row in result]

    def create(self, user_dict):
        new_user = UserData(**user_dict)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return convert_model_to_json(new_user, UserData)
    
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
