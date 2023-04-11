import bcrypt

class UserDataService():

    def get_all_user(self, model):
        return model.get_all_user()
    
    def delete_by_id(self, user_id, model):
        if user_id is None:
            return None, -1, "user id is none"
        
        user, _, _ = model.get_by_id(user_id)

        if user is None:
            return None, -1, "Get user fail"
        
        return model.delete(user_id)
    
    def get_by_id(self, user_id, model):
        if user_id is None:
            return None, -1, "user id is none"
        
        return model.get_by_id(user_id)
    
    def update(self, user_id, data, model):
        if user_id is None:
            return None, -1, "user id is none"
        
        return model.update(user_id, data)
    
    def reset_password(self, data, model):
        filter = {"ResetPasswordToken": data["reset_password_token"]}
        data['new_password'] = self.__encode_password(data['new_password'])
        update = {"Password": data["new_password"]}
        
        user, _, _ = model.get_by(filter)
        if user is None:
            return None, -1, "User not exist"
        
        count, _, _ = model.update(user.Id, update)
        if count > 0:
            return self._reset_token_none(user.Id, model)

        return None, -1, "Reset password fail"
    
    def _reset_token_none(self, user_id, model):
        set_reset_password_token_none = {"ResetPasswordToken": None}
        return model.update(user_id, set_reset_password_token_none)
    
    def update_password(self, user_id, data, model):
        user, _, _ = model.get_by_id(user_id)

        if user is None:
            return None, -1, 'User not exist'

        if self.__compare_password(data['old_password'], user.Password) == -1:
            return None, -1, 'Password not correct'
        
        data['new_password'] = self.__encode_password(data['new_password'])
        update = {"Password": data["new_password"]}
        
        return model.update(user_id, update)

    def create(self, user_dict: dict, model):
        user_dict['Password'] = self.__encode_password(user_dict['Password'])
        return model.create(user_dict)

    def login(self, user_dict, model):
        stored_user, code, _ = model.get_by({'Email': user_dict['email'], 'activate': True})

        if code == -1:
            return None, -1, 'username wrong'
        
        if self.__compare_password(user_dict['password'], stored_user.Password) == -1:
            return None, -1, 'wrong password'
            
        return stored_user, 0, 'login success'

    def __encode_password(self, password: str):
        salt = bcrypt.gensalt()
        return  bcrypt.hashpw(password.encode('utf-8'), salt)
    
    def __compare_password(self, password: str, stored_password: str):
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            return 0
        else:
            return -1
