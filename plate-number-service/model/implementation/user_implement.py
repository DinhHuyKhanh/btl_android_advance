

from model.repository.user_repository import UserRepository


class UserImplement():
    
    def __init__(self) -> None:
        pass
    
    def get_all_user(self):
        return UserRepository().get_all_users()
    
    def register(self, user_dict):
        return UserRepository().create(user_dict)
    
    def get_user_by_email(self, email: str):
        return UserRepository().get_user_by_email(email)