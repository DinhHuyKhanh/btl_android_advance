from datetime import datetime
from decimal import Decimal

from model.implementation.user_implement import UserImplement

from model.implementation.transaction_implement import TransactionImplement

from util.constants import TransactionMsg

class PaymentService():
    def __init__(self) -> None:
        self.transaction_imp = TransactionImplement()

    def handle_car_payment(self, gate_history):
        try:

            timestamp = gate_history['CheckOutDate'].timestamp() - gate_history['CheckInDate'].timestamp()
            coin = Decimal((timestamp/3600)*1000)

            user_data, code, _ = self.__update_coin_user(gate_history['UserId'], coin)
            if user_data is None or code == -1:
                return None, -1, 'User not found'

            transaction_data = {
                "UserId": gate_history['UserId'],
                "Coin": -coin,
                "LastCoin": user_data['Coin']+coin,
                "CreatedDate": datetime.now(),
                "Description": TransactionMsg.CAR_DEPOSIT_PAYMENT.value
            }

            return self.transaction_imp.create(transaction_data)
        except Exception as e:
            return None, -1, f'Exception as: {str(e)}'

    def __update_coin_user(self, user_id, coin):
        user_imp = UserImplement()
        user_data, code, msg = user_imp.get_by_id(user_id)
        if (user_data is None) or code == -1:
            return None, -1, 'User not found'
        if user_data['Coin'] < coin:
            return None, -1, 'user coin less than coin payment'
        user_data['Coin'] -= coin
        user_update, code ,msg = user_imp.update(user_id, user_data)
        if code == -1:
            return None, -1, 'update fail'
        return user_data, code, msg
        
        
        