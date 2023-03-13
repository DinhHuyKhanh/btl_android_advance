

from model.repository.user_repository import UserRepository


class UserImplement():
    
    def __init__(self) -> None:
        pass
    
    def get_all_user(self):
        return UserRepository().get_all_users()