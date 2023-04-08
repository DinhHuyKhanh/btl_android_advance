
from app.service.detect_plate_service import DetectPlateService
from app.service.user_service import UserService
from model.implementation.user_implement import UserImplement
from app.service.email_service import MailService

#SERVICE
user_service = UserService()
PlateService = DetectPlateService
mail_service = MailService()


#MODEL
user_model = UserImplement()