from model.models import GateHistory
from model.repository.gate_history_repository import GateHistoryRepository


class GateHistoryImplement():
    
    def __init__(self) -> None:
        self.gate_history_imp = GateHistoryRepository()

    
    def get_all_gate_histories(self, user_id):
        filter = {"UserId": user_id}
        items = self.gate_history_imp.get_all_gate_histories(filter)
        if items is None: 
            return None, -1, 'get all gate history not found'
        return items, 0, 'success'
    
    def create(self, data):
        data = GateHistory(**data)
        item = self.gate_history_imp.create(data)
        if item is None:
            return None, -1, 'create gate history faild'
        return item, 0, 'success'

    def get_last_plate(self, number_plate):
        last_plate_history = self.gate_history_imp.get_last_plate(number_plate)
        if last_plate_history is None: 
            return None, -1, 'get last plate history fail'
        return last_plate_history, 0, 'success'
    
    def update(self, data):
        new_history = self.gate_history_imp.update(data)
        if new_history is None:
            return None, -1, 'update gate history fail'
        return new_history, 0, 'success'

    def count_gate_history(self):
        return self.gate_history_imp.count_gate_history()
    
    def get_all(self, params):
        return self.gate_history_imp.get_all(params)