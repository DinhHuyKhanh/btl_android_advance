from model.models import GateHistory
from model.repository.gate_history_repository import GateHistoryRepository


class GateHistoryImplement():
    
    def __init__(self) -> None:
        pass
    
    def get_all_gate_histories(self, user_id):
        filter = {"UserId": user_id}
        return GateHistoryRepository().get_all_gate_histories(filter)
    
    def create(self, data):
        return GateHistoryRepository().create(GateHistory(**data))
