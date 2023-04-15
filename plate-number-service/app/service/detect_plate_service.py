import os
import shutil
import cv2
from paddleocr import PaddleOCR
from conf import SAVE_MODEL, STATIC_MEDIA
from starlette.datastructures import UploadFile
import time

class DetectPlateService():

    def __init__(self) -> None:
        self.net = cv2.dnn.readNetFromDarknet(f'{SAVE_MODEL}/yolov4-tiny-custom.cfg', f'{SAVE_MODEL}/yolov4-tiny-custom_best.weights')
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')
        self.model = cv2.dnn_DetectionModel(self.net)
        self.model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
        pass

    def save_local(self, image: UploadFile):
        os.makedirs(STATIC_MEDIA, exist_ok=True)
        file_name = f'{time.time()}_{image.filename}'
        image_url = f'{STATIC_MEDIA}/{file_name}'
        with open(image_url, 'wb') as buffer:
            shutil.copyfileobj(image.file, buffer)
        return file_name

    def save_image_by_name(self, file_name, image: UploadFile):
        image_url = f'{STATIC_MEDIA}/{file_name}'
        with open(image_url, 'wb') as buffer:
            shutil.copyfileobj(image.file, buffer)
        return file_name

    def detect_plate(self, image: UploadFile):
        file_name = self.save_local(image)
        ans, code, msg = self.handle_detect(file_name)

        return ans, code, "success"

    def handle_detect(self, file_name):
        try:
            image_url = f'{STATIC_MEDIA}/{file_name}'
            image_cv2 = cv2.imread(image_url)
            classIds, scores, boxes = self.model.detect(image_cv2, confThreshold=0.6, nmsThreshold=0.4)
            ans=None
            for (classId, score, box) in zip(classIds, scores, boxes):
                cv2.rectangle(image_cv2, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),color=(0, 255, 0), thickness=2)
                cv2.imwrite(image_url, image_cv2)
                img2 = image_cv2[box[1]:box[1] + box[3], box[0]:box[0] + box[2]]
                result = self.ocr.ocr(img2, cls=True)
                ans= f"{result[0][0][-1][0]} {result[0][1][-1][0]}"
            return ans, 0, "success"
        except Exception as e:
            return None, -1, f"exception as {str(e)}"

    def register(self, user_id, image: UploadFile, model):
        try: 
            file_name = self.save_local(image)
            plate_txt, code, msg = self.handle_detect(file_name)
            new_plate = {
                'UserId': user_id,
                'NumberPlate': plate_txt,
                'ImagePath': file_name
            }

            return model.register(new_plate)
            
        except Exception as e:
            return None, -1, f"exception as {str(e)}"
        
    def update(self, id, image: UploadFile, model):
        try:
            plate, code, msg = model.get_plate_by_id(id)
            if code == -1:
                return plate, code, msg
            file_name = self.save_image_by_name(plate['ImagePath'], image)
            plate_txt, code, msg = self.handle_detect(file_name)
            if code == -1:
                return None, code, msg
            plate['NumberPlate'] = plate_txt
            return model.update(id, plate)
        except Exception as e:
            return None, -1, f'exception as {str(e)}'







