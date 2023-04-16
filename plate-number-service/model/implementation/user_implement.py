from model.models import UserData
from model.interface.user_model import UserModel
from model.repository.user_repository import UserRepository


class UserImplement(UserModel):
    
    def __init__(self) -> None:
        self.user_repository = UserRepository()


    def get_all_user(self, limit, offset, sort = 'asc'):
        return self.user_repository.get_all_users(limit, offset, sort)
    
    def create(self, data):
        return UserRepository().create(UserData(**data))
    
    def get_by_id(self, id):
        filter = {"activate": True}
        return UserRepository().get(id, filter)
    
    def delete(self, id):
        filter = {"activate": False}
        return UserRepository().update(id, filter)
    
    def update(self, id, filter):
        return UserRepository().update(id, filter)
    
    def get_and_update(self, filter, update):
        return UserRepository().get_by_and_update(filter, update)
    
    def get_by(self, filter):
        return UserRepository().get_by(filter)

    def get_user_by_email(self, email: str):
        return self.user_repository.get_user_by_email(email)
    
    def count_user(self):
        return self.user_repository.count_user()
