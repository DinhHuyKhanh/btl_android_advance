import bcrypt

class UserDataService():

    def get_all_user(self, limit, offset, sort, model):
        try:
            items = model.get_all_user(limit, offset, sort)
            total = model.count_user()
            page= offset
            return total, page, limit, items, 0, 'success'
        except Exception as e:
            return None, None, None,None,  -1, f'Exception as {str(e)}'
    
    def delete_by_id(self, user_id, model):
        try:
            if user_id is None:
                return None, -1, "user id is none"
            
            user = model.get_by_id(user_id)

            if user is None:
                return None, -1, "Get user fail"
            
            count = model.delete(user_id)

            if count > 0:
                return count, 0, 'Delete user success'
        
            return count, -1, 'Delete user fail'
        except Exception as e:
            return None,  -1, f'Exception as {str(e)}' 
    
    def get_by_id(self, user_id, model):
        try:
            if user_id is None:
                return None, -1, "user id is none"
            
            user = model.get_by_id(user_id)

            if user is None:
                return None, -1, "Get user fail"
            
            return user, 0, "Get user success"
        except Exception as e:
            return None,  -1, f'Exception as {str(e)}' 
    
    def update(self, user_id, data, model):
        try:
            if user_id is None:
                return None, -1, "user id is none"
            
            count = model.update(user_id, data)

            if count > 0:
                return count, 0, "Update success"
            return None, -1, "Update fail"
        except Exception as e:
            return None,  -1, f'Exception as {str(e)}' 
    
    def reset_password(self, data, model):
        try:
            filter = {"ResetPasswordToken": data["reset_password_token"]}
            data['new_password'] = self.__encode_password(data['new_password'])
            update = {"Password": data["new_password"]}
            
            user = model.get_by(filter)
            if user is None:
                return None, -1, "User not exist"
            
            count = model.update(user.Id, update)
            if count > 0:
                return self._reset_token_none(user.Id, model)

            return None, -1, "Reset password fail"
        except Exception as e:
            return None,  -1, f'Exception as {str(e)}' 
    
    def _reset_token_none(self, user_id, model):
        set_reset_password_token_none = {"ResetPasswordToken": None}
        count = model.update(user_id, set_reset_password_token_none)

        if count > 0:
            return count, 0, "Update success"
        return None, -1, "Update fail"
    
    def update_password(self, user_id, data, model):
        try:
            user = model.get_by_id(user_id)

            if user is None:
                return None, -1, 'User not exist'

            if self.__compare_password(data['old_password'], user.Password) == -1:
                return None, -1, 'Password not correct'
            
            data['new_password'] = self.__encode_password(data['new_password'])
            update = {"Password": data["new_password"]}
            
            count = model.update(user_id, update)
            if count > 0:
                return count, 0, "Update success"
            return None, -1, "Update fail"
        except Exception as e:
            return None,  -1, f'Exception as {str(e)}' 

    def create(self, user_dict: dict, model):
        try:
            user_dict['Password'] = self.__encode_password(user_dict['Password'])
            user = model.create(user_dict)

            if user is None:
                return None, -1, "Create user fail"
            
            return user, 0, "Create user success"
        except Exception as e:
            return None,  -1, f'Exception as {str(e)}' 

    def login(self, user_dict, model):
        try:
            stored_user = model.get_by({'Email': user_dict['email'], 'activate': True})

            if stored_user is None:
                return None, -1, 'username wrong'
            
            if self.__compare_password(user_dict['password'], stored_user.Password) == -1:
                return None, -1, 'wrong password'
                
            return stored_user, 0, 'login success'
        except Exception as e:
            return None,  -1, f'Exception as {str(e)}' 

    def __encode_password(self, password: str):
        salt = bcrypt.gensalt()
        return  bcrypt.hashpw(password.encode('utf-8'), salt)
    
    def __compare_password(self, password: str, stored_password: str):
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            return 0
        else:
            return -1
