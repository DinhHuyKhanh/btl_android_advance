import random
import string
from util.constants import Code

class MailService():
    def create_code(self, email, model):
        reset_password_token = self._get_random_string(Code.LENGTH_CODE)
        filter = {"email": email, "activate": True}
        update = {"resetpasswordtoken": reset_password_token}
        model.get_and_update(filter, update)

        return reset_password_token
    
    def _get_random_string(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        
        return result_str