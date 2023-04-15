import logging
from model.repository.base_repository import BaseRepository
from model.models import GateHistory

logger = logging.getLogger()

class GateHistoryRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()

    def get_all_gate_histories(self, filter=None):
        try:
            gate_history = self.db.query(GateHistory).filter_by(**filter).all()
            if gate_history is None:
                return None, -1, "Get gate histories fail"
            
            return gate_history, 0, "Get gate histories success"
        except Exception as e:
            logger.exception(e)
            return None, -1, "Get histories fail"
    
    def create(self, data):
        try:
            self.db.add(data)
            self.db.commit()
            self.db.refresh(data)
            
            return data, 0, "Create gate history success"
        except Exception as e:
            logger.exception(e)
            return None, -1, "Create gate history fail"
