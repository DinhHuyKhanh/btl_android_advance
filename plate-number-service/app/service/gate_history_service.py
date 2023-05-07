from app.service.payment_service import PaymentService
from model.implementation.gate_history_implement import GateHistoryImplement
from model.implementation.plate_implement import PlateImplement
from datetime import date, timedelta, datetime


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
                 'CheckInDate': datetime.now(),
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
            if not gate_history or gate_history['CheckOutDate']:
                return self.create(number_plate, file_name)
            gate_history['ImagePathCheckOut'] = file_name
            gate_history['CheckOutDate'] = datetime.now()
            payment_service = PaymentService()
            car_payment, code, msg = payment_service.handle_car_payment(gate_history)
            gate_history['Coin'] = -car_payment['Coin']
            if code == -1:
                return None, -1, msg
            return self.gate_hist_imp.update(gate_history)
        except Exception as e:
            return None, -1, f'exception as {str(e)}'

    def get_all(self,limit, offset, sort, start_date, end_date , model):
        try:
            if end_date is None:
                start_date = date.today() -  timedelta(days=90)
                end_date = date.today()
            params = {
                'limit': limit,
                'offset': offset,
                'sort': sort,
                'start_date': str(start_date),
                'end_date': str(end_date)
            }
            items = model.get_all(params)
            total = model.count_gate_history()
            page = params['offset']
            return total, page, params['limit'], items, 0, 'success'
        except Exception as e:
            return None, None, None, None,  -1, f'Exception as {str(e)}'
