from fastapi import APIRouter, File, UploadFile
from pydantic import FilePath
from app.controller.schema import ImageRequest
from app.settings import PlateModel, PlateService
from conf import STATIC_MEDIA
from util.helper import wrap_responses
from fastapi.responses import FileResponse
from fastapi import Path


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
    return PlateService().update(id, image, PlateModel())

@router.get('/{image_path}')
async def read_img(image_path: str = Path(..., description="Full path of the image")):
    image_full_path = f'{STATIC_MEDIA}/{image_path}'
    return FileResponse(image_full_path)


@router.get('/find_by_id/{id}')
@wrap_responses
async def get_plate_by_id(id: int):
    return PlateModel().get_plate_by_id(id)