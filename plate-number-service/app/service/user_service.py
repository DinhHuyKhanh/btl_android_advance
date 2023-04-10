

class UserService():

    def get_all_user(self, model):
        return model.get_all_user()
    
    def create(self, data, model):
        return model.create(data)
    
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
        filter = {"resetpasswordtoken": data["reset_password_token"]}
        update = {"password": data["new_password"]}
        
        user, _, _ = model.get_by(filter)
        if user is None:
            return None, -1, "User not exist"
        
        count, _, _ = model.update(user.id, update)
        if count > 0:
            return self._reset_token_none(user.id, model)

        return None, -1, "Reset password fail"
    
    def _reset_token_none(self, user_id, model):
        set_reset_password_token_none = {"resetpasswordtoken": None}
        return model.update(user_id, set_reset_password_token_none)
    
    def update_password(self, user_id, data, model):
        filter = {"id": user_id, "password": data["old_password"]}
        update = {"password": data["new_password"]}
        
        return model.get_and_update(filter, update)