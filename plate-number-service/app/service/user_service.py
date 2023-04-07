

class UserService():

    def get_all_user(self, model):
        return model.get_all_user()
    
    def create(self, data, model):
        return model.create(data)
    
    def delete(self, id, model):
        filter = {"activate": False}
        return model.update(id, filter)
    
    def get_by_id(self, id, model):
        return model.get_by_id(id)