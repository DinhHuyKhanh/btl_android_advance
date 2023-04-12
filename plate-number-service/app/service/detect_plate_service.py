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

    def save_local(self, image: UploadFile, static_path: str):
        os.makedirs(static_path, exist_ok=True)
        image_url = f'{static_path}/{time.time()}_{image.filename}'
        with open(image_url, 'wb') as buffer:
            shutil.copyfileobj(image.file, buffer)
        return image_url

    def save_image_by_path(self, image_url, image: UploadFile):
        with open(image_url, 'wb') as buffer:
            shutil.copyfileobj(image.file, buffer)
        return image_url

    def detect_plate(self, image: UploadFile):
        static_path = f'{STATIC_MEDIA}/save_images/'
        image_url = self.save_local(image, static_path)
        ans, code, msg = self.handle_detect(image_url)

        return ans, code, "success"

    def handle_detect(self, image_url):
        try:
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
            static_path = f'{STATIC_MEDIA}/image_plate_register'
            image_url = self.save_local(image, static_path)
            plate_txt, code, msg = self.handle_detect(image_url)
            new_plate = {
                'UserId': user_id,
                'NumberPlate': plate_txt,
                'ImagePath': image_url
            }

            return model.register(new_plate)
            
        except Exception as e:
            return None, -1, f"exception as {str(e)}"
        
    def update(self, id, image: UploadFile, model):
        try:
            plate, code, msg = model.get_plate_by_id(id)
            if code == -1:
                return plate, code, msg
            image_url = self.save_image_by_path(plate['ImagePath'], image)
            plate_txt, code, msg = self.handle_detect(image_url)
            if code == -1:
                return None, code, msg
            plate['NumberPlate'] = plate_txt
            return model.update(id, plate)
        except Exception as e:
            return None, -1, f'exception as {str(e)}'







