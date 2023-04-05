from fastapi import APIRouter, File, UploadFile
from app.settings import PlateService
from util.helper import wrap_responses


router = APIRouter(
    prefix='/plates',
    tags=['plates']
)

@router.post('')
@wrap_responses
async def detect_plate(image: UploadFile = File(...)):
    return PlateService().detect_plate(image)
