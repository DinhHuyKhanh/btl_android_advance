import bcrypt
from app.service.payment_service import PaymentService

class UserDataService():

    def get_all_user(self, limit, offset, sort, model):
        try:
            items = model.get_all_user(limit, offset, sort)
            total = model.count_user()
            page = offset
            return total, page, limit, items, 0, 'success'
        except Exception as e:
            return None, None, None, None,  -1, f'Exception as {str(e)}'
    
    def delete_by_id(self, user_id, model):
        try:
            if user_id is None:
                return None, -1, "user id is none"
            
            user, _, _ = model.get_by_id(user_id)

            if user is None:
                return None, -1, "Get user fail"
            
            return model.delete(user_id)
        except Exception as e:
            return None,  -1, f'Exception as {str(e)}' 
    
    def get_by_id(self, user_id, model):
        try:
            if user_id is None:
                return None, -1, "user id is none"
            
            return model.get_by_id(user_id)
        except Exception as e:
            return None,  -1, f'Exception as {str(e)}' 
    
    def update(self, user_id, data, model):
        try:
            if user_id is None:
                return None, -1, "user id is none"
            
            return model.update(user_id, data)
        except Exception as e:
            return None,  -1, f'Exception as {str(e)}' 
    
    def reset_password(self, data, model):
        try:
            filter = {"ResetPasswordToken": data["reset_password_token"]}
            data['new_password'] = self.__encode_password(data['new_password'])
            update = {"Password": data["new_password"]}
            
            user, _, _ = model.get_by(filter)
            if user is None:
                return None, -1, "User not exist"
            
            count, _, _ = model.update(user.Id, update)
            if count > 0:
                return self.__reset_token_none(user.Id, model)

            return None, -1, "Reset password fail"
        except Exception as e:
            return None,  -1, f'Exception as {str(e)}' 
    
    def __reset_token_none(self, user_id, model):
        set_reset_password_token_none = {"ResetPasswordToken": None}
        return model.update(user_id, set_reset_password_token_none)
    
    def update_password(self, user_id, data, model):
        try:
            user,_, _ = model.get_by_id(user_id)

            if user is None:
                return None, -1, 'User not exist'

            if self.__compare_password(data['old_password'], user["Password"]) == -1:
                return None, -1, 'Password not correct'
            
            data['new_password'] = self.__encode_password(data['new_password'])
            update = {"Password": data["new_password"]}
            
            return model.update(user_id, update)
        except Exception as e:
            return None,  -1, f'Exception as {str(e)}' 

    def create(self, user_dict: dict, model):
        try:
            user_dict['Password'] = self.__encode_password(user_dict['Password'])
            return model.create(user_dict)
        except Exception as e:
            return None,  -1, f'Exception as {str(e)}' 

    def login(self, user_dict, model):
        try:
            stored_user, _, _ = model.get_by({'Email': user_dict['email'], 'activate': True})

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

    def add_money(self, user_id, data, model):
        try:
            user, _, _ = model.get_by_id(user_id)

            if user is None:
                return None, -1, 'User not exist'

            update = {"Coin": data["money"] + user['Coin']}

            payment_service = PaymentService()
            car_payment, code, msg = payment_service.add_money(user_id, data["money"])

            if car_payment is None:
                return None, -1, 'Car not exist'

            return model.update(user_id, update)
        except Exception as e:
            return None, -1, f'Exception as {str(e)}'
