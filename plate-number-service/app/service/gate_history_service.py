from app.service.payment_service import PaymentService
from model.implementation.gate_history_implement import GateHistoryImplement
from model.implementation.plate_implement import PlateImplement
import datetime


class GateHistoryService():

    def __init__(self) -> None:
        self.gate_hist_imp = GateHistoryImplement()

    def get_all_gate_histories(self, user_id, model):
        return model.get_all_gate_histories(user_id)
    
    def create(self,number_plate, file_name):
            plate_imp = PlateImplement()
            stored_plate, code ,msg = plate_imp.get_by_number_plate(number_plate)
            if not number_plate or code == -1:
                 return None, code, msg
            plate = {
                 'UserId': stored_plate['UserId'],
                 'NumberPlate': stored_plate['NumberPlate'],
                 'CheckInDate': datetime.datetime.now(),
                 'ImagePathCheckIn': file_name
                }
            return self.gate_hist_imp.create(plate)
    
    def create_or_update(self, number_plate, file_name):
        try:
            gate_history, code, msg = self.gate_hist_imp.get_last_plate(number_plate)
            if len(gate_history) == 0:
                gate_history = None 
            else: 
                gate_history = gate_history[0]
            if (not gate_history or gate_history['CheckOutDate']):
                return self.create(number_plate, file_name)
            gate_history['ImagePathCheckOut'] = file_name
            gate_history['CheckOutDate'] = datetime.datetime.now()

            payment_service = PaymentService()
            car_payment = payment_service.handle_car_payment(gate_history)
            return  self.gate_hist_imp.update(gate_history)
        except Exception as e:
            return None, -1, f'exception as {str(e)}'
