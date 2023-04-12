from fastapi import APIRouter, File, UploadFile
from app.settings import PlateModel, PlateService
from util.helper import wrap_responses


router = APIRouter(
    prefix='/plates',
    tags=['plates']
)

@router.post('')
@wrap_responses
async def detect_plate(image: UploadFile = File(...)):
    return PlateService().detect_plate(image)


@router.post('/{user_id}')
@wrap_responses
async def register_plate(user_id: int, image: UploadFile = File(...)):
    return PlateService().register(user_id, image, PlateModel())

@router.put('/{id}')
@wrap_responses
async def update_plate(id: int, image: UploadFile = File(...)):
    print("id", id)
    return PlateService().update(id, image, PlateModel())
 
