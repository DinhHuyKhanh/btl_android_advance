
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

