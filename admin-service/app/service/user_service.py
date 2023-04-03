from model.models import User

class UserService():

    def get_all_user(self, model):
        return model.get_all_user()

    def create_user(self, user, model):
        return model.create_user(user)

    def authenticate_user(self, login_from, model):
        return model.authenticate_user(login_from)
