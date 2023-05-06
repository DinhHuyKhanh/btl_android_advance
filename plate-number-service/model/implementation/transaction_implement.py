
from model.repository.transaction_history import TransactionRepository
from model.interface.transaction_model import TransactionModel


class TransactionImplement(TransactionModel):

    def __init__(self) -> None:
        super().__init__()
        self.transaction_repository = TransactionRepository()

    def create(self, transaction):
        transaction_stored = self.transaction_repository.createTransaction(transaction)
        if transaction_stored is None:
            return None, -1, 'create transaction fail'
        return transaction_stored, 0, 'create transaction success'

    def get_all_by(self, filter=None):
        transactions = self.transaction_repository.get_all_by(filter)
        if transactions is None:
            return None, -1, 'get transactions fail'
        return transactions, 0, 'get transactions success'

    def get_transactions_by_month_and_year(self, month, year, filter=None):
        transactions = self.transaction_repository.get_transactions_by_month_and_year(month, year, filter)
        if transactions is None:
            return None, -1, 'get transactions fail'
        return transactions, 0, 'get transactions success'