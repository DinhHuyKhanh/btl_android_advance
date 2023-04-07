

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
    
    def get_by_id(self, id, model):
        return model.get_by_id(id)