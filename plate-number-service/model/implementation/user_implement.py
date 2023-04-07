from model.models import DbUser
from model.repository.user_repository import UserRepository


class UserImplement():
    
    def __init__(self) -> None:
        pass
    
    def get_all_user(self):
        filter = {"activate": True}
        return UserRepository().get_all_users(filter)
    
    def create(self, data):
        return UserRepository().create(DbUser(**data))
    
    def get_by_id(self, id):
        filter = {"activate": True}
        return UserRepository().get(id, filter)
    
    def update(self, id, filter):
        return UserRepository().update(id, filter)
    