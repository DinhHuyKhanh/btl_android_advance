
from app.service.detect_plate_service import DetectPlateService
from app.service.user_service import UserDataService
from model.implementation.user_implement import UserImplement
from model.implementation.gate_history_implement import GateHistoryImplement
from app.service.email_service import MailService
from app.service.gate_history_service import GateHistoryService

#SERVICE
UserService = UserDataService
PlateService = DetectPlateService
mail_service = MailService()
GateService = GateHistoryService


#MODEL
UserModelImp = UserImplement
GateHistoryModelImp = GateHistoryImplement
