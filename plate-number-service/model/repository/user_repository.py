from sqlalchemy.orm.session import Session
from model.database import SessionLocal, get_db
from model.models import DbUser

class UserRepository():

    def __init__(self) -> None:
        self.db = SessionLocal()

    def get_all_users(self):
        return self.db.query(DbUser).all()
    
    def create(self, data):
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        
        return data
    
    def get_by_id(self, id):
        return self.db.get(DbUser, id)
    
    def update(self, id, filter):
        data = self.db.query(DbUser).filter_by(id = id)
        count = data.update(filter)
        self.db.commit()

        return count