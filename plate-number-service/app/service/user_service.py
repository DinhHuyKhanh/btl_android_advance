import bcrypt

class UserDataService():

    def get_all_user(self, model):
        return model.get_all_user()
    
    def register(self, user_dict: dict, model):
        user_dict['Password'] = self.__encode_password(user_dict['Password'])
        return model.register(user_dict)

    def login(self, user_dict, model):
        stored_user, code, msg = model.get_user_by_email(user_dict['email'])
        if code == -1:
            return None, -1, 'username wrong'
        if self.__decode_password(user_dict['password'], stored_user['Password']) == -1:
            return None, -1, 'wrong password'
        del stored_user['Password']
        return stored_user, 0, 'login success'

    def __encode_password(self, password: str):
        salt = bcrypt.gensalt()
        return  bcrypt.hashpw(password.encode('utf-8'), salt)
    
    def __decode_password(self, password: str, stored_password: str):
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            return 0
        else:
            return -1
        