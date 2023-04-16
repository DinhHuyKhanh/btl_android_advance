

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
        return convert_model_to_json(new_plate, NumberPlate)

    def get_by_id(self, id):
        number_plate = self.db.query(NumberPlate).filter_by(Id=id).first()
        self.db.close()
        if not number_plate:
            return None
        return convert_model_to_json(number_plate, NumberPlate)

    def update(self,id ,plate):
        plate_stored = self.db.query(NumberPlate).filter_by(Id=id).first()
        plate_stored.NumberPlate = plate['NumberPlate']
        self.db.commit()
        self.db.refresh(plate_stored)
        self.db.close()
        return convert_model_to_json(plate_stored, NumberPlate)

    def get_by_number_plate(self, number_plate):
        number_plate = self.db.query(NumberPlate).filter_by(NumberPlate=number_plate).first()
        self.db.close()
        return convert_model_to_json(number_plate, NumberPlate)