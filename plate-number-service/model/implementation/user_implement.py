

from model.repository.user_repository import UserRepository


class UserImplement():
    
    def __init__(self) -> None:
        self.user_repository = UserRepository()

    
    def get_all_user(self):
        return self.user_repository.get_all_users()
    
    def register(self, user_dict):
        return self.user_repository.create(user_dict)
    
    def get_user_by_email(self, email: str):
        return self.user_repository.get_user_by_email(email)