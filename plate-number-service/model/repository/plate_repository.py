

from model.models import NumberPlate
from model.repository.base_repository import BaseRepository
from util.utils import convert_model_to_json


class PlateRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()
    
    def createPlate(self, plate):
        new_plate = NumberPlate(**plate)
        self.db.add(new_plate)
        self.db.commit()
        self.db.refresh(new_plate)
        return convert_model_to_json(new_plate, NumberPlate), 0, "success"

    def get_by_id(self, id):
        number_plate = self.db.query(NumberPlate).filter_by(Id=id).first()
        self.db.close()
        if not number_plate:
            return None, -1, 'Number Plate not found'
        return convert_model_to_json(number_plate, NumberPlate), 0, "success"

    def update(self,id ,plate):
        plate_stored = self.db.query(NumberPlate).filter_by(Id=id).first()
        plate_stored.NumberPlate = plate['NumberPlate']
        self.db.commit()
        self.db.refresh(plate_stored)
        self.db.close()
        return convert_model_to_json(plate_stored, NumberPlate), 0, "success"
    
    def get_all(self, user_id, limit=None, offset=None):
        return self.db.query(NumberPlate).filter_by(UserId=user_id).order_by(NumberPlate.Id).limit(limit).offset(offset).all()
