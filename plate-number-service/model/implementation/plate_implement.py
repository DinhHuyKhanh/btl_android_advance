
from pydantic import (
    BaseModel as PydanticBaseModel, ValidationError,
    validator)
from model.interface.plate_model import PlateModel

from model.repository.plate_repository import PlateRepository


class PlateValidator(PydanticBaseModel):
    UserId: int
    NumberPlate: str
    ImagePath: str

    @validator('NumberPlate', 'ImagePath')
    def prevent_empty_str(cls, v):
        if v is None:
            return v

        if v.strip() == '':
            raise ValueError('field should not be empty')
        return v.strip()


class PlateImplement(PlateModel):

    def __init__(self) -> None:
        super().__init__()
        self.plate_repository = PlateRepository()

    def build_item(self, item):
        try:
            validated_data = PlateValidator(**item)
            return validated_data.dict(), 0, 'Item is validated'
        except ValidationError as e:
            raise ValueError(str(e))

    def register(self, plate):
        plate, code, msg = self.build_item(plate)
        if code == -1: 
            return None, code, msg 
        new_plate = self.plate_repository.createPlate(plate)
        if new_plate is None:
            return None, -1, 'create plate fail'
        return new_plate, 0, 'success'

    def get_plate_by_id(self, id):
        item = self.plate_repository.get_by_id(id)
        if item is None: 
            return None, -1, 'item not found'
        return item, 0, 'success'
    
    def update(self,id, plate):
        new_item = self.plate_repository.update(id, plate)
        if new_item is None: 
            return None, -1, 'update fail'
        return new_item, 0, 'success'
    
    def get_all(self, user_id, limit=None, offset=None):
        plates = self.plate_repository.get_all(user_id, limit, offset)
        if plates is None:
            return None, None, -1, "Get all plates fail"
        
        return plates, len(plates), 0, 'Get all plates success'
    
    def get_by_number_plate(self, plate_number):
        stored_data = self.plate_repository.get_by_number_plate(plate_number)
        if stored_data is None: 
            return None, -1, 'fail'
        return stored_data, 0, 'success'
    
