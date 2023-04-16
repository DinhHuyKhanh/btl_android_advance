
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
        return self.plate_repository.createPlate(plate)

    def get_plate_by_id(self, id):
        return self.plate_repository.get_by_id(id)
    
    def update(self,id, plate):
        return self.plate_repository.update(id, plate)
    