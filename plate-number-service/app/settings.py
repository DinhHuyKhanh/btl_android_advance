
from app.service.detect_plate_service import DetectPlateService
from app.service.user_service import UserService
from model.implementation.user_implement import UserImplement

#SERVICE
user_service = UserService()
PlateService = DetectPlateService


#MODEL
user_model = UserImplement()