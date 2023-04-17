from model.models import UserData
from model.interface.user_model import UserModel
from model.repository.user_repository import UserRepository


class UserImplement(UserModel):
    
    def __init__(self) -> None:
        self.user_repository = UserRepository()


    def get_all_user(self, limit, offset, sort = 'asc'):
        return self.user_repository.get_all_users(limit, offset, sort)
    
    def create(self, data):
        new_user = UserRepository().create(UserData(**data))
        if new_user is None:
            return None, -1, "Create user fail"
        
        return new_user, 0, "Create user success"
    
    def get_by_id(self, id):
        filter = {"activate": True}
        item = UserRepository().get(id, filter)
        if item is None:
            return None, -1, 'Get user fail'
        return item, 0, 'Get user success'
    
    def delete(self, id):
        filter = {"activate": False}
        count = UserRepository().update(id, filter)
        if not count:
            return None, -1, 'Delete fail'
        return count, 0, 'Delete success'
    
    def update(self, id, filter):
        count = UserRepository().update(id, filter)
        if not count:
            return None, -1, 'Update fail'
        return count, 0, 'Update success'
    
    def get_and_update(self, filter, update):
        item = UserRepository().get_by_and_update(filter, update)
        if item:
            return item, 0, 'Update success'
        return None, -1, 'Update fail' 
    
    def get_by(self, filter):
        item = UserRepository().get_by(filter)
        if item is None:
            return item, -1, 'Get user fail'
        return item, 0, 'Get user success'

    def get_user_by_email(self, email: str):
        item = self.user_repository.get_user_by_email(email)
        if item is None: 
            return None, -1, 'Get user fail'
        return item, 0, 'Get user success'
    
    def count_user(self):
        return self.user_repository.count_user()