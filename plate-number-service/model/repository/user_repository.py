import logging
from model.database import SessionLocal
from model.models import DbUser

logger = logging.getLogger()

class UserRepository():

    def __init__(self) -> None:
        self.db = SessionLocal()

    def get_all_users(self, filter=None):
        try:
            users = self.db.query(DbUser).filter_by(**filter).all()
            if users is None:
                return None, -1, "Get users fail"
            
            return users, 0, "Get users success"
        except Exception as e:
            logger.exception(e)
            return None, -1, "Get users fail"
    
    def create(self, data):
        try:
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            
            return data, 0, "Create user success"
        except Exception as e:
            logger.exception(e)
            return None, -1, "Create user fail"
        
    def get(self, id, filter=None):
        try:
            if id is None:
                return None
            if not filter:
                filter = {}

            filter["id"] = id
            
            user = self.db.query(DbUser).filter_by(**filter).first()

            if user is None:
                return None, -1, "Get user fail"
            
            return user, 0, "Get user success"
        except Exception as e:
            logger.exception(e)
            return None, -1, "Get user fail"
        
    def get_by(self, filter):
        try:
            user = self.db.query(DbUser).filter_by(**filter).first()

            if user is None:
                return None, -1, "Get user fail"
            
            return user, 0, "Get user success"
        except Exception as e:
            logger.exception(e)
            return None, -1, "Get user fail"
        
    def get_by_and_update(self, filter, update):
        try:
            data = self.db.query(DbUser).filter_by(**filter)
            count = data.update(update)
            self.db.commit()

            if count == 1:
                return count, 0, "Update success"
            return None, -1, "Update fail"
        except Exception as e:
            logger.exception(e)
            return None, -1, "Update fail"
    
    def update(self, id, filter):
        try:
            data = self.db.query(DbUser).filter_by(id=id)
            count = data.update(filter)
            self.db.commit()

            if count == 1:
                return count, 0, "Update success"
            return None, -1, "Update fail"
        except Exception as e:
            logger.exception(e)
            return None, -1, "Update fail"