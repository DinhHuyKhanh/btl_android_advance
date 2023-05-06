from sqlalchemy import func
import sqlalchemy
from model.models import TransactionHistory
from model.repository.base_repository import BaseRepository
from util.utils import convert_model_to_json, convert_tuple_to_list


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
        transactions = self.db.query(func.month(TransactionHistory.CreatedDate), func.year(TransactionHistory.CreatedDate)).distinct().filter_by(**filter).all()
        return convert_tuple_to_list(transactions)
    
    def get_transactions_by_month_and_year(self, month, year, filter=None):
        transactions = self.db.query(TransactionHistory).filter(
                sqlalchemy.extract('year', TransactionHistory.CreatedDate) == year,
                sqlalchemy.extract('month', TransactionHistory.CreatedDate) == month
            ).filter_by(**filter).all()
        return transactions