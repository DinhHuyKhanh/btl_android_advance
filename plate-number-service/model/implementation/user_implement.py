from model.interface.user_model import UserModel
from model.repository.user_repository import UserRepository


class UserImplement(UserModel):
    
    def __init__(self) -> None:
        self.user_repository = UserRepository()

    
    def get_all_user(self, limit, offset, sort = 'asc'):
        return self.user_repository.get_all_users(limit, offset, sort), 0, 'success'
    
    def register(self, user_dict):
        return self.user_repository.create(user_dict)
    
    def get_user_by_email(self, email: str):
        return self.user_repository.get_user_by_email(email), 0, 'success'
    
    def count_user(self):
        return self.user_repository.count_user(), 0, 'success'
