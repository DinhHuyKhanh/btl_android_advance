from model.models import GateHistory
from model.repository.gate_history_repository import GateHistoryRepository


class GateHistoryImplement():
    
    def __init__(self) -> None:
        pass
    
    def get_all_gate_histories(self, user_id):
        filter = {"UserId": user_id}
        items = GateHistoryRepository().get_all_gate_histories(filter)
        if items is None: 
            return None, -1, 'get all gate history not found'
        return items, 0, 'success'
    
    def create(self, data):
        data = GateHistory(**data)
        item = GateHistoryRepository().create(data)
        if item is None:
            return None, -1, 'create gate history faild'
        return item, 0, 'success'

    def get_last_plate(self, number_plate):
        last_plate_history = GateHistoryRepository().get_last_plate(number_plate)
        if last_plate_history is None: 
            return None, -1, 'get last plate history fail'
        return last_plate_history, 0, 'success'
    
    def update(self, data):
        new_history = GateHistoryRepository().update(data)
        if new_history is None:
            return None, -1, 'update gate history fail'
        return new_history, 0, 'success'
