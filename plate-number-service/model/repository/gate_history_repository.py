import logging
from util.utils import convert_model_to_json
from sqlalchemy import text
from model.repository.base_repository import BaseRepository
from model.models import GateHistory
from util.constants import TableNames

class GateHistoryRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()

    def get_all_gate_histories(self, filter=None):
        gate_history = self.db.query(GateHistory).filter_by(**filter).all()
        if gate_history is None:
            return None
        return gate_history
        
    
    def create(self, data):
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)

        return data

    def get_last_plate(self, number_plate):
        with self.db as session: 
            result = session.execute(text(
                f"""
                SELECT Id, UserId, NumberPlate, CheckInDate,
                CheckOutDate, ImagePathCheckIn, ImagePathCheckOut
                FROM {TableNames.GATE_HISTORY.value}
                ORDER BY CheckInDate DESC
                LIMIT 1
                """
            ).params(
                number_plate=number_plate,
            ))
            return [dict(row) for row in result]
        
    def update(self, data):
        stored_data = self.db.query(GateHistory).filter_by(Id=data['Id']).update(data)
        self.db.commit()
        self.db.close()
        if stored_data == 1:
            return stored_data
        return None
    
    def get_all(self, params):
        with self.db as session:
            result = session.execute(text(
                f"""
                    SELECT Id, UserId, NumberPlate, CheckInDate, CheckOutDate, ImagePathCheckIn, ImagePathCheckOut, Coin
                    FROM {TableNames.GATE_HISTORY.value}
                    WHERE CheckInDate BETWEEN :start_date and :end_date
                    ORDER BY Id {params['sort']}
                    LIMIT :limit 
                    OFFSET :offset
                """
            ).params(
                limit=params['limit'],
                offset=params['offset']*params['limit'],
                end_date=params['end_date'],
                start_date=params['start_date']
            ))
            rows= [dict(row) for row in result.fetchall()]
            return rows
    def count_gate_history(self):
        count = self.db.query(GateHistory).count()
        if not count: 
            count = 0
        return count

