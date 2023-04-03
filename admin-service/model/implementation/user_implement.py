
from model.repository.user_repository import UserRepository
from model.models import User


class UserImplement():

    def __init__(self) -> None:
        pass

    def get_all_user(self):
        return UserRepository().get_all_users()

    def create_user(self, user: User) -> User:
        return UserRepository().create_user(user)

    def authenticate_user(self, login_model) -> User:
        email = login_model["email"]
        password = login_model["password"]

        return UserRepository().authenticate_user(email, password)
