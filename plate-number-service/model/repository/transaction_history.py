from model.models import TransactionHistory
from model.repository.base_repository import BaseRepository
from util.utils import convert_model_to_json


class TransactionRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()
    
    def createTransaction(self, transaction):
        new_transaction = TransactionHistory(**transaction)
        self.db.add(new_transaction)
        self.db.commit()
        self.db.refresh(new_transaction)
        return convert_model_to_json(new_transaction, TransactionHistory)
    
    def get_all_by(self, filter=None):
        transactions = self.db.query(TransactionHistory).filter_by(**filter).all()
        return transactions