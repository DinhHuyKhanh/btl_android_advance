import logging
from model.database import SessionLocal
from model.models import DbUser

logger = logging.getLogger()

class UserRepository():

    def __init__(self) -> None:
        self.db = SessionLocal()

    def get_all_users(self, filter=None):
        try:
            return self.db.query(DbUser).filter_by(**filter).all()
        except Exception as e:
            logger.exception(e)
            return None
    
    def create(self, data):
        try:
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            
            return data
        except Exception as e:
            logger.exception(e)
            return None
        
    def get(self, id, filter=None):
        try:
            if id is None:
                return None
            if not filter:
                filter = {}

            filter["id"] = id
            
            return self.db.query(DbUser).filter_by(**filter).first()
        except Exception as e:
            logger.exception(e)
            return None
        
    def get_by_and_update(self, filter, update):
        try:
            data = self.db.query(DbUser).filter_by(**filter)
            count = data.update(update)
            self.db.commit()

            return count
        except Exception as e:
            logger.exception(e)
            return None
    
    def update(self, id, filter):
        try:
            data = self.db.query(DbUser).filter_by(id=id)
            count = data.update(filter)
            self.db.commit()

            return count
        except Exception as e:
            logger.exception(e)
            return -1