

class UserService():

    def get_all_user(self, model):
        return model.get_all_user()
    
    def create(self, data, model):
        return model.create(data)
    
    def delete_by_id(self, user_id, model):
        if user_id is None:
            return -1
        
        user = model.get_by_id(user_id)

        if user is None:
            return -1
        
        return model.delete(user_id)
    
    def get_by_id(self, user_id, model):
        if user_id is None:
            return None
        
        return model.get_by_id(user_id)
    
    def update(self, user_id, data, model):
        if user_id is None:
            return -1
        
        return model.update(user_id, data)
    
    def reset_password(self, data, model):
        filter = {"resetpasswordtoken": data["reset_password_token"], "password": data["old_password"]}
        update = {"password": data["new_password"]}
        
        user = model.get_by(filter)
        if user is None:
            return -1
        
        count = model.update(user.id, update)
        if count > 0:
            return self._reset_token_none(user.id, model)

        return -1
    
    def _reset_token_none(self, user_id, model):
        set_reset_password_token_none = {"resetpasswordtoken": None}
        return model.update(user_id, set_reset_password_token_none)