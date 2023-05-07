from enum import Enum

class TableNames(Enum):
    USER_DATA = "user_data"
    GATE_HISTORY = "gate_history"

class Code(Enum):
    LENGTH_CODE = 8

class TransactionMsg(Enum):
    CAR_DEPOSIT_PAYMENT="car deposit payment"
    DEPOSITING="depositing"
    CAR_CREDIT_PAYMENT = "car credit payment"
    CREDITING = "crediting"
