
from app.service.detect_plate_service import DetectPlateService
from app.service.user_service import UserDataService
from model.implementation.user_implement import UserImplement
from app.service.email_service import MailService

#SERVICE
UserService = UserDataService
PlateService = DetectPlateService
mail_service = MailService()


#MODEL
UserModelImp = UserImplement