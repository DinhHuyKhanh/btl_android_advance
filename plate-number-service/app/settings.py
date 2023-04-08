
from app.service.detect_plate_service import DetectPlateService
from app.service.user_service import UserDataService
from model.implementation.user_implement import UserImplement

#SERVICE
UserService = UserDataService
PlateService = DetectPlateService


#MODEL
UserModelImp = UserImplement