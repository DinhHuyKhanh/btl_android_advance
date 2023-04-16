
class UserModel():
    def get_all_users(self):
        raise NotImplementedError
    
    def create(self, user_dict):
        raise NotImplementedError
    
    def get_user_by_email(self, email: str):
        raise NotImplementedError
    
    def count_user(self):
        raise NotImplementedError