
from app.service.plate_service import PlateService
from app.service.user_service import UserDataService
from model.implementation.plate_implement import PlateImplement
from model.implementation.user_implement import UserImplement
from model.implementation.gate_history_implement import GateHistoryImplement
from app.service.email_service import MailService
from app.service.qr_code_service import QrCodeService
from app.service.gate_history_service import GateHistoryService
from model.implementation.transaction_implement import TransactionImplement
from app.service.transaction_history_service import TransactionHistoryService

#SERVICE
UserService = UserDataService
PlateService = PlateService
mail_service = MailService()
qr_code_service = QrCodeService
GateService = GateHistoryService
TransactionService = TransactionHistoryService


#MODEL
UserModelImp = UserImplement
GateHistoryModelImp = GateHistoryImplement
PlateModel = PlateImplement
TransactionHistoryImplement = TransactionImplement
