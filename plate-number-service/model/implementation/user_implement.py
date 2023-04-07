from model.models import DbUser
from model.repository.user_repository import UserRepository


class UserImplement():
    
    def __init__(self) -> None:
        pass
    
    def get_all_user(self):
        return UserRepository().get_all_users()
    
    def create(self, data):
        return UserRepository().create(DbUser(**data))
    
    def get_by_id(self, id):
        return UserRepository().get_by_id(id)
    
    def update(self, id, filter):
        return UserRepository().update(id, filter)
    